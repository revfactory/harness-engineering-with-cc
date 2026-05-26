# 풀스택 팀 8 에이전트 표

| name | 역할 | model | tools | 활성 Phase |
|------|------|-------|-------|------------|
| feature-pm | 요구사항 분해 · Phase 할당 · 통합 대시보드 | opus | TeamCreate, TaskCreate, AgentTool, SendMessage, TeamDelete, Read, Write | 0·1·2·3·4 |
| api-designer | 엔드포인트 · 응답 구조 · 인증 흐름 정의 | opus | Read, Write, Grep, SendMessage | 1 |
| ui-designer | 화면 플로우 · 컴포넌트 트리 · 상태 머신 · 폼 유효성 | opus | Read, Write, Grep, SendMessage | 1 |
| db-migrator | users 테이블 · 인덱스 · 마이그레이션 SQL 초안 | opus | Read, Write, Grep, SendMessage | 1 |
| backend-impl | API 코드 · 단위 테스트 · 마이그레이션 실행 | sonnet | Read, Write, Edit, Bash, SendMessage | 2 |
| frontend-impl | 페이지 · 훅 · 상태 코드 · MSW mock | sonnet | Read, Write, Edit, Bash, SendMessage | 2 |
| boundary-verifier | API ↔ 훅 데이터 구조 · 라우팅 · 상태 전이 교차 검증 | opus | Read, Grep, SendMessage | 2·3 |
| test-suite | E2E 시나리오 · 회귀 테스트 생성 (서브에이전트) | sonnet | Read, Write, Bash | 4 |

## 핵심 도구 부여 근거

- `backend-impl` / `frontend-impl`만 **Edit / Bash** 보유 — 실제 코드 수정 + 빌드/테스트 실행 권한이 있는 두 워커.
- `boundary-verifier`에 **Edit 미부여** — "verifier의 역할은 문제 검증이지 수정이 아니다" (책 본문). 판정 후 수정은 `backend-impl` 또는 `frontend-impl`에게 SendMessage로 위임.
- `api-designer` / `ui-designer` / `db-migrator`는 **설계만** — Edit 없음, Write만 (설계 문서 작성).
- `test-suite`는 **PM 단독 수신** — SendMessage 미부여. PM이 AgentTool로 호출한다.

## 팀 규모

총 8명이지만 Phase별 동시 활성은 4명 이내 (`01_phase_matrix.md`).

> 세션당 한 팀, Phase당 3~4개의 에이전트를 유지하는 게 좋습니다.
