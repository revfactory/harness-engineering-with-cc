# 8 에이전트 모델 채택 근거

| 에이전트 | model | 채택 근거 |
|---------|-------|----------|
| feature-pm | opus | 라이프사이클 전체 의사결정 + Phase 게이트 판정 — 추론 부담 큼 |
| api-designer | opus | 엔드포인트 + 인증 흐름 + 응답 스키마 동시 추론 |
| ui-designer | opus | 페이지 트리 + 상태 머신 + 폼 유효성 동시 추론 |
| db-migrator | opus | 스키마 + 인덱스 + 제약 + 마이그레이션 SQL 동시 추론 |
| backend-impl | sonnet | 명세는 확정된 상태. 단일 파일 단위 코드 작성 (속도·비용 우선) |
| frontend-impl | sonnet | 명세는 확정된 상태. 단일 파일 단위 코드 작성 |
| boundary-verifier | **opus (예외)** | 두 산출물 동시 추론 부담 + 판정 결과의 파급 큼 |
| test-suite | sonnet | 5 시나리오 패턴이 반복적. opus 불필요 |

## 분포

- **opus 5명**: 설계 3 + PM + boundary-verifier (예외)
- **sonnet 3명**: 구현 2 + test-suite

## 핵심 인용

> 구현 에이전트(backend-impl·frontend-impl)는 한 번에 한 파일 단위로 작업하므로 sonnet으로 충분합니다. 그러나 boundary-verifier는 양쪽 파일을 동시에 추론해야 하므로 opus가 필요합니다.

— 두 파일 동시 추론 부담이 verifier에 opus를 부여하는 근거.

## 팀 규모 원칙

> 세션당 한 팀, Phase당 3~4개의 에이전트를 유지하는 게 좋습니다.

총 8명이지만 Phase별 동시 활성 최대 4명 (`01_phase_matrix.md`).
