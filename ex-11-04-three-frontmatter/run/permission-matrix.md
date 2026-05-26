# 권한 차등 검증 매트릭스

> 본 sub-harness는 mock 산출만 작성. 권한 검증은 .md 정의 기준 + mock 보고서 내 도구 사용 흔적 기준.

| 에이전트 | Bash 부여 | Bash 시도 (mock) | Edit 부여 | Edit 시도 (mock) | 결과 |
|---------|---------|---------------|---------|---------------|------|
| static-analyzer | ✓ | tsc, eslint | ✗ | 0 | 정합 |
| security-auditor | ✓ | npm audit, semgrep | ✗ | 0 | 정합 |
| design-reviewer | ✗ | 0 | ✗ | 0 | 정합 (Bash·Edit 모두 0) |
| refactorer | ✗ | 0 | ✓ | `_workspace/patches/*.diff` 2회 | 정합 (대상 화이트리스트 한정) |

## 위반 시 차단 시나리오 (정의 기준)
- design-reviewer가 Bash를 시도하면: 정의에 없으므로 호출 거부.
- refactorer가 `src/api/users.ts` Edit 시도하면: Edit는 부여돼 있으나 시스템 레벨로 대상 경로 검증 필요 (CLAUDE.md 규칙 + 호출자 사전 점검).
- 누구든 git commit 시도: 어떤 에이전트도 git 부여 안 했으므로 자동 차단.

## 핵심 정합 포인트
- Edit 단독 부여(refactorer)
- Bash 차등(static·security만)
- 자동 커밋 금지(누구도 git 권한 없음)
