---
name: pr-review-orchestrator
description: "PR·diff·변경 파일 목록을 받아 정적 분석, 보안 검토, 테스트 영향 검토를 병렬로 수행하고 하나의 리뷰 리포트로 통합한다. 사용자가 'PR 리뷰', 'diff 점검', '변경사항 리뷰', '코드 리뷰 자동화'를 요청하면 이 스킬을 사용한다. 단일 파일의 간단한 스타일 조언은 code-reviewer 스킬로 처리하고, 전체 코드베이스 보안 감사는 security-auditor 스킬로 위임한다."
allowed-tools: ["Read", "Grep", "Glob", "Bash"]
---
# PR Review Orchestrator


## 목표
변경사항 하나를 네 에이전트 팀으로 검토한다. 오케스트레이터는 직접 코드를 고치지 않는다.
팀을 만들고, 작업 큐를 배치하고, 팀원 간 직접 메시지를 허용하고, 최종 리포트만 통합한다.


## 입력
- `diff_path` 또는 PR diff 텍스트
- 변경 파일 목록
- 선택 입력: 리뷰 기준, 금지된 변경 영역, 릴리스 위험도


## 산출물
- `_workspace/pr-review/static.md`
- `_workspace/pr-review/security.md`
- `_workspace/pr-review/tests.md`
- `_workspace/pr-review/final-review.md`
- `_workspace/pr-review/team-log.jsonl`


## Phase 0. 사전 조건
1. 변경 파일 목록을 읽고 리뷰 범위를 확정한다.
2. `_workspace/pr-review/` 디렉터리 존재를 확인한다.
3. diff가 없거나 변경 파일이 0개면 사용자에게 중단 사유를 보고한다.
4. 파일 수가 40개를 넘으면 먼저 범위를 나누고, 이번 실행에서는 가장 위험도가 높은 묶음 하나만 리뷰한다.


## Phase 1. 팀 생성
TeamCreate로 `pr-review-team`을 만든다.
팀원 네 명을 AgentTool로 스폰한다.


| 이름 | 역할 | 출력 |
|------|------|------|
| static-reviewer | 버그·성능·스타일 검토 | `_workspace/pr-review/static.md` |
| security-reviewer | 입력 검증·권한·비밀 노출 검토 | `_workspace/pr-review/security.md` |
| test-reviewer | 테스트 영향·누락 회귀 검토 | `_workspace/pr-review/tests.md` |
| review-integrator | 세 리포트 병합·중복 제거 | `_workspace/pr-review/final-review.md` |


각 팀원 프롬프트에는 공통 규칙을 넣는다.
- 발견 즉시 관련 팀원에게 SendMessage로 알린다.
- 최종 판단은 파일에 저장한다.
- Critical 발견 시 오케스트레이터와 관련 팀원에게 동시에 보고한다.
- 코드 수정은 하지 않는다.


## Phase 2. 작업 큐 배치
TaskCreate로 네 작업을 만든다.


1. `static-pass`: static-reviewer 담당. diff 전체의 버그·성능·스타일 검토.
2. `security-pass`: security-reviewer 담당. 외부 입력·권한·비밀 노출 검토.
3. `test-pass`: test-reviewer 담당. 변경 파일과 테스트 매핑, 누락 테스트 검토.
4. `integrate-review`: review-integrator 담당. 앞 세 작업 완료 후 실행. `depends_on = ["static-pass", "security-pass", "test-pass"]`.


## Phase 3. 팀원 간 메시지 규칙
SendMessage는 리더를 거치지 않는다.


- static-reviewer가 데이터 구조(shape) 변경을 발견하면 test-reviewer에게 테스트 영향 확인을 요청한다.
- security-reviewer가 인증·권한 변경을 발견하면 test-reviewer에게 보안 회귀 테스트 존재 여부를 묻는다.
- test-reviewer가 테스트 불가능한 설계를 발견하면 static-reviewer에게 구조 리스크 확인을 요청한다.
- Critical 이슈는 오케스트레이터에도 요약 메시지를 보낸다.


메시지 형식은 고정한다.


```json
{
    "type": "finding",
    "severity": "Critical|High|Medium|Low",
    "file": "path/to/file.ts",
    "line": 42,
    "claim": "문제를 주장하는 한 문장",
    "request": "상대 팀원이 확인할 질문"
}
```


## Phase 4. 통합 게이트
review-integrator는 세 리포트를 모두 읽고 다음 순서로 통합한다.


1. Critical·High를 먼저 배치한다.
2. 같은 원인의 중복 이슈는 하나로 합친다.
3. 증거가 없는 제안은 제외한다.
4. 테스트 누락만 있는 항목은 "권고"로 낮추고, 실제 버그 증거가 있으면 "차단"으로 올린다.
5. 최종 리포트에는 `must-fix`, `should-fix`, `watch` 세 섹션만 둔다.


## Phase 5. 종료
1. 네 팀원에게 `shutdown_request`를 SendMessage로 보낸다.
2. 각 팀원이 진행 중 파일 쓰기를 끝냈는지 확인한다.
3. TeamDelete로 팀을 해체한다.
4. `_workspace/pr-review/team-log.jsonl`에 팀 생성·작업 배치·종료 시각을 append-only로 남긴다.


## 실패 처리
- 팀원 1명 실패: 같은 역할을 한 번 재시도한다.
- 같은 팀원 2회 실패: 해당 리포트 누락을 final-review에 명시하고 진행한다.
- 팀원 2명 이상 실패: TeamDelete 후 사용자에게 중단 보고한다.
- Critical 발견: 나머지 리뷰는 계속하되 최종 판정은 `must-fix`를 포함한 차단 상태로 둔다.
- TeamDelete 실패: 숨기지 않고 수동 정리 필요 항목을 보고한다.


## 최종 응답 형식
사용자에게는 세 가지만 보고한다.
1. 차단 이슈 수와 파일 위치.
2. 권고 이슈 수.
3. 전체 리포트 경로 `_workspace/pr-review/final-review.md`.
