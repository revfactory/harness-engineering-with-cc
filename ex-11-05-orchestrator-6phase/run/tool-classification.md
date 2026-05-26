# 도구 분류: 공식 5종 vs 의사 함수 4종

## 공식 (Claude Code 환경에서 실 호출 가능)

| 도구 | 사용처 | 비고 |
|------|--------|------|
| TeamCreate | Phase 1 | 팀 부트스트랩. 1회. |
| AgentTool | Phase 1 | 4회 (worktree isolation). |
| TaskCreate | Phase 2 | 4회 for-루프. 4번째에 depends_on. |
| SendMessage | Phase 3 | 워커 정의(.md)에서 동료 간 호출. 리더 미경유. |
| TeamDelete | Phase 5 | 팀 해체. workspace는 보존. |

## 의사 함수 (구현자가 직접 만들어야 함)

| 함수 | 시그니처 | 실 구현 힌트 |
|------|---------|-------------|
| `parseDiff(diff)` | `(text) -> { files: [{path, hunks:[...]}, ...] }` | `parse-diff` npm 패키지 or 자체 정규식 |
| `waitForTeamCompletion(teamId, opts)` | `(id, {tasks: string[]}) -> Promise<void>` | TaskStatus 폴링 or 이벤트 구독 |
| `mergeReports(reports, opts)` | `(string[], {priority: string[]}) -> string` | 마크다운 파싱 + 우선순위 정렬 (ex-11-07에 실 구현 스니펫) |
| `$` | `` `(cmd) -> Promise<string>` `` | `child_process.execSync` 또는 zx 라이브러리 |

## 운영 메모
- 본 SKILL.md를 그대로 복사해 다른 환경에 옮길 때는 의사 함수 4종을 먼저 채워야 한다.
- `mergeReports`의 실 구현 예시는 ex-11-07의 `built/scripts/merge-reports.ts` 참조.
