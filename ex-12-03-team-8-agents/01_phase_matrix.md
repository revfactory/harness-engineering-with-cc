# Phase × 에이전트 활성 매트릭스

| 에이전트 \ Phase | 0 | 1 | 2 | 3 | 4 |
|------------------|---|---|---|---|---|
| feature-pm       | O | O | O | O | O |
| api-designer     | . | O | . | . | . |
| ui-designer      | . | O | . | . | . |
| db-migrator      | . | O | . | . | . |
| backend-impl     | . | . | O | O | . |
| frontend-impl    | . | . | O | O | . |
| boundary-verifier| . | . | O | O | . |
| test-suite       | . | . | . | . | O |

## Phase 설명

| Phase | 목적 | 활성 (PM 제외 워커 수) |
|-------|------|-----------------------|
| 0 | 요구사항 분해 (PM 단독) | 0 |
| 1 | 설계 팬아웃 (api / ui / db 삼각) | 3 |
| 2 | 구현 + 상시 검증 (back / front / verifier) | 3 |
| 3 | 잔여 결함 수정 (Phase 2 연장) | 3 |
| 4 | 통합 + E2E (test-suite) | 1 |

## 동시 활성 상한

- Phase 1, 2, 3: 워커 3명 + PM = **4명** (책 "Phase당 3~4개" 부합).
- Phase 0, 4: 더 적게 (1~2명).
- 동시 활성이 5명 이상이면 **세션을 분할**하거나 일부 에이전트의 시작을 지연.

## test-suite 별도 처리

test-suite은 Phase 4에만 활성, **PM 단독 수신**. TeamCreate으로 워커 팀에 포함시키지 않고, PM이 AgentTool로 직접 호출한다. 다른 에이전트와 동시 활성 금지.
