# 하네스엔지니어링 with Claude Code — 예제 모음

> 책 **《하네스엔지니어링 with Claude Code》** 의 실습 예제 저장소입니다.
> [한빛미디어 도서 페이지](https://www.hanbit.co.kr/store/books/look.php?p_code=B2817272480)

Claude Code를 "한 번의 대화를 잘 굴리는 도구"가 아니라 **작업 환경(=하네스)을 미리 세팅해두는 도구** 로 다루기 위한 실습들을 챕터·절 단위로 묶어 두었습니다. 각 예제 폴더에는 자체 `README.md` 가 들어 있으니 실행 방법과 결과 비교는 해당 폴더의 문서를 참고하세요.

---

## 예제 인덱스

| 예제 | 주제 | 설명 |
|---|---|---|
| **2장 — 첫 하네스** | | |
| [`ex-02-01-ab-comparison`](./ex-02-01-ab-comparison) | 하네스 적용 전/후 A/B 비교 | 동일한 한 줄 프롬프트(`claude code 사용 팁 정리해주세요`)를 **맨몸**과 **하네스 적용** 두 가지 방식으로 실행한 결과를 2단 페이지로 비교합니다. |
| [`ex-02-02-my-first-harness`](./ex-02-02-my-first-harness) | 첫 하네스 — 2인 팀 커밋 메시지 | `commit-msg-author` 와 `commit-msg-reviewer` 두 에이전트, 이들을 순차 호출하는 `commit-message` 스킬로 구성한 최소 하네스. 스테이지된 변경을 받아 Conventional Commits 메시지를 author·reviewer 협업으로 생성합니다. |
| **4장 — 에이전트 설계** | | |
| [`ex-04-01-security-analyst`](./ex-04-01-security-analyst) | 읽기 전용 보안 분석 에이전트 | `tools` 에서 `Write`/`Edit` 을 의도적으로 제외해 **수정 권한을 물리적으로 차단**한 `security-analyst`. 취약점을 심은 Flask 샘플 앱에 적용해 심각도·위치·권장 수정안 형식의 보고서를 산출합니다. |
| [`ex-04-02-copy-editor`](./ex-04-02-copy-editor) | 기계적 교정 에이전트 — 1단계 검수 | 산문 끝 콜론·Bold 한글 조사·명백한 오탈자 3종만 기계적으로 잡는 `copy-editor`. 위반을 심은 가상 원고에 적용해 처리 요약·파일별 내역·보류 항목 리포트를 만듭니다. |
| **5장 — 스킬 디자인 원리** | | |
| [`ex-05-05-separation-signals`](./ex-05-05-separation-signals) | 스킬 분리 3 신호 진단 | 크기·도메인 분기·조건부 상세 3 신호 표를 옮기고, `skill-size-auditor` 가 3 샘플 SKILL.md를 진단해 신호 발현을 정확히 잡는지 검증합니다. |
| [`ex-05-06-domain-references`](./ex-05-06-domain-references) | 도메인 분기형 references — 메뉴판/레시피 | SKILL.md는 조건부 링크만 두고 도메인 본문은 `references/` 로 위임하는 패턴을 mermaid + 실물 `sql-query` 스킬 + 호출 트레이스 2건으로 시각화합니다. |
| [`ex-05-08-generalization`](./ex-05-08-generalization) | 일반화 vs 오버피팅 — 재적용 실측 | Overfit / Generalized SKILL.md 2개로 7건 테스트 열에 N=3 반복 적용해 적용률을 비교하는 dry-run 시뮬레이션입니다. |
| [`ex-05-09-context-savings`](./ex-05-09-context-savings) | 컨텍스트 절약 3 원칙 가지치기 | 3 원칙을 옮기고 `prose-pruner` 가 의도 설계된 위반 샘플에서 원칙별 위반을 진단·가지치기한 결과를 30% 이상 축약으로 보입니다. |
| [`ex-05-10-book-writer-skill`](./ex-05-10-book-writer-skill) | book-writer 종합 사례 + 3 원리 매핑 | 두 버전의 `book-writer` 프론트매터를 발췌·diff하고 Pushy·Layer·Why-First 3 원리로 매핑한 뒤 본 저장소 스킬을 진단해 미니 템플릿까지 산출합니다. |
| [`ex-05-11-with-without`](./ex-05-11-with-without) | With/Without 스킬 비교 1 사이클 | `csv-summary` 스킬 1건에 With/Without 를 동시 실행(`&`+`wait`)하고 `pass_rate`·`duration_ms`·`total_tokens` 3축으로 비교, 변별력 있는/없는 단언 반례까지 산출합니다. |
| [`ex-05-12-antipatterns`](./ex-05-12-antipatterns) | 스킬 안티패턴 3종 진단 | 거대 SKILL.md / references 부재 / 이유 없는 규칙 3 안티패턴을 옮기고, `antipattern-detector` 가 의도 위반 3 샘플을 진단·심각도 라벨링합니다. |
| **6장 — PR 리뷰 오케스트레이션** | | |
| [`ex-06-12-pr-review-skill-md`](./ex-06-12-pr-review-skill-md) | `pr-review-orchestrator` SKILL.md 실물 | 책 SKILL.md 전문을 `.claude/skills/pr-review-orchestrator/SKILL.md` 로 보존하고 4인 에이전트 stub과 dry-run 결과를 동봉합니다. |
| [`ex-06-15-292-agent-incident`](./ex-06-15-292-agent-incident) | 292개 에이전트 사건 — 정량 검증 | 책의 채널 수 폭주 사례를 인용 + 정량 데이터 + 외부 자료 교차 검증 메모로 정리한 사례 노트입니다. |
| **7장 — 에이전트 정의 실물** | | |
| [`ex-07-13-phase3-agent-5sections`](./ex-07-13-phase3-agent-5sections) | Phase 3 에이전트 정의 — 8 섹션 완비 | `security-reviewer.md` 를 8 섹션 완비 버전으로 작성하고 5 필수 vs 7~8 섹션 비교를 제공합니다. |
| **8장 — 안전장치** | | |
| [`ex-08-15-max-retries-code`](./ex-08-15-max-retries-code) | `MAX_RETRIES` 안전장치 — 실행 가능 코드 | 책의 의사코드 + 더미 generator/verifier 로 실제 실행이 가능하며, 성공/실패 2 시나리오 로그를 산출합니다. |
| **11장 — 코드 리뷰 팀** | | |
| [`ex-11-03-static-analyzer-md`](./ex-11-03-static-analyzer-md) | `static-analyzer` 에이전트 + 샘플 TS PR | 책 본문의 `static-analyzer.md` 와 호출 대상 sample TS PR을 보존, mock 모드 기본 + `tsc`·`eslint` 화이트리스트로 경계를 강제합니다. |
| [`ex-11-04-three-frontmatter`](./ex-11-04-three-frontmatter) | 4인 팀 — 3 에이전트 frontmatter 공존 | `security` / `design` / `refactor` 3 에이전트 실물(+ ex-11-03 의 `static-analyzer` 복사)로 4인 팀을 구성하고 도구 경계를 frontmatter로 강제합니다. |
| [`ex-11-05-orchestrator-6phase`](./ex-11-05-orchestrator-6phase) | `code-review-team` 6 Phase dry-run | 책 의사코드를 SKILL.md로 마감하고 6 Phase mock 오케스트레이션 로그를 산출합니다. |
| [`ex-11-06-jwt-pr-bugs`](./ex-11-06-jwt-pr-bugs) | JWT PR + 의도 버그 4종 + 4인 팀 (mock) | SQL 인젝션·N+1·경계면 불일치·테스트 0건 4 버그를 심은 JWT 리프레시 PR에 mock 4 리뷰어를 적용해 발견 매트릭스·Without/With 비교를 만듭니다. |
| **12장 — 풀스택 팀** | | |
| [`ex-12-03-team-8-agents`](./ex-12-03-team-8-agents) | 풀스택 8 에이전트 + Phase 활성 매트릭스 | PM·api·ui·db·backend·frontend·boundary·test 8 에이전트 정의에 모델·도구 경계를 frontmatter로 강제, Phase별 동시 활성 ≤4명을 매트릭스로 관리합니다. |
| **13장 — 의존성 분석** | | |
| [`ex-13-01-dependency-mapper`](./ex-13-01-dependency-mapper) | 의존성 그래프 → 결정론적 배치 계획 | `Read, Grep, Bash` 만으로 동작하는 `dependency-mapper` 가 `sample-src/` import 그래프를 분석해 위상정렬 결과를 `batches.json` 으로 산출. 기본 mock 모드, `USE_LIVE_LLM=1` 에서 실제 sonnet 호출. |
| **14장 — 응용 가이드** | | |
| [`ex-14-10-application-guide`](./ex-14-10-application-guide) | 4 응용 가이드 매핑 — Post-mortem · 플래키 · 성능 · 1인 | 4 application-*.md + `reviewer.md` frontmatter(Post-mortem 전용)와 매핑·교차 참조 정리. 본격 구현은 ex-14-11 (플래키) / ex-14-12 (성능) 로 위임됩니다. |

> 추가 예제는 챕터 진행에 따라 같은 컨벤션으로 계속 추가될 예정입니다.

---

## 시작하기

```bash
# 1. 저장소 클론
git clone https://github.com/revfactory/harness-engineering-with-cc.git
cd harness-engineering-with-cc

# 2. 원하는 예제 폴더로 이동
cd ex-02-01-ab-comparison

# 3. 폴더 안의 README를 따라 실습 진행
open README.md
```

Claude Code 설치 및 기본 사용법은 [공식 문서](https://docs.claude.com/en/docs/claude-code/overview) 를 참고하세요.

---

## 라이선스

이 저장소의 코드 예제는 [Apache License 2.0](./LICENSE) 을 따릅니다. 책의 본문·도판 등 출판물 콘텐츠 자체의 저작권은 저자 및 한빛미디어에 귀속됩니다.
