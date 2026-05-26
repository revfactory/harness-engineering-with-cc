# 책 의사코드 vs SKILL.md 충실도

## 책 핵심 호출 (p192-194)

| 호출 | 책 | 우리 | diff |
|------|----|----|------|
| `TeamCreate({ name: "code-review", ... })` | 있음 | 있음 | 0 |
| `AgentTool` × 4 (worktree) | 있음 | 있음 (`isolation: "worktree"`) | 0 |
| `TaskCreate` × 4 (for-루프) | 있음 | 있음 (`for (const t of taskSpecs)`) | 0 |
| `depends_on: ["정적 분석", "설계 검토", "보안 감사"]` | 있음 | 있음 (한글 그대로) | 0 |
| `mergeReports(reports, { priority: ["P0","P1","P2"] })` | 있음 | 있음 | 0 |
| `gh pr comment ${prNumber} -F ...review_report.md` | 있음 | 있음 | 0 |
| `TeamDelete` + workspace 보존 명시 | 있음 | 있음 | 0 |

## roleMap 배열

책: `["static-analyzer","design-reviewer","security-auditor","refactorer"]`
우리: 동일 (순서 보존).

## 의사 함수 4종 보존
- `parseDiff` ✓
- `waitForTeamCompletion` ✓
- `mergeReports` ✓
- `$` (셸 헬퍼) ✓

## diff 평가
- 의사코드 변수명·키워드 변경 0
- "workspace 보존" 표현 보존
- 자동 커밋 금지 명시 보존
