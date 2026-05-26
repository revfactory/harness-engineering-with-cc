---
name: code-review-team
description: PR diff에 대해 정적분석·설계·보안 3 리뷰어 + 리팩토러 4인 팀을 운영한다. 트리거 - "코드 리뷰", "PR 리뷰", "리뷰 재실행", "다시 실행", "리뷰 보고서".
allowed-tools: TeamCreate, AgentTool, TaskCreate, SendMessage, TeamDelete, Read, Write, Bash(gh pr diff, gh pr comment)
---

# code-review-team

> 4인 리뷰어 팀 오케스트레이터. 리더는 텍스트를 쓰지 않는다 — 워커 4인이 모든 보고서를 생산한다.

## 사용 시점
- PR 번호가 주어지고 코드 리뷰를 요청받았을 때
- "리뷰 재실행", "다시 실행" 같이 동일 PR을 같은 팀으로 재돌릴 때
- 사용자가 "코드 리뷰 팀 만들어줘" 같이 책 11장 팀을 직접 지칭할 때

## 6 Phase 워크플로 (의사코드)

> 공식 도구: TeamCreate, AgentTool, TaskCreate, SendMessage, TeamDelete.
> 의사 함수 (실 구현 필요): `parseDiff`, `waitForTeamCompletion`, `mergeReports`, `$` (셸 실행 헬퍼).

```typescript
async function codeReviewTeam(prNumber: number) {
  // ──────────────────────────────────────────────
  // Phase 0 — 입력 수집
  // ──────────────────────────────────────────────
  const diff = await $(`gh pr diff ${prNumber}`);  // 의사: $
  await Write(`_workspace/input/pr-${prNumber}.diff`, diff);
  const parsed = parseDiff(diff);                  // 의사: parseDiff

  // ──────────────────────────────────────────────
  // Phase 1 — TeamCreate + AgentTool × 4 (worktree 격리)
  // ──────────────────────────────────────────────
  const team = await TeamCreate({
    name: "code-review",
    description: "PR diff를 4개 렌즈로 리뷰한다"
  });

  const roleMap = [
    "static-analyzer",
    "design-reviewer",
    "security-auditor",
    "refactorer"
  ];
  for (const role of roleMap) {
    await AgentTool({
      team: team.id,
      agent: role,
      isolation: "worktree"
    });
  }

  // ──────────────────────────────────────────────
  // Phase 2 — TaskCreate × 4 (for-루프)
  // ──────────────────────────────────────────────
  // 책 주의: 단건 호출은 TaskCreate 1회씩이지만, 의사 표기로는 배열 표기로도 자주 그려진다.
  // 실제로는 for-루프로 4회 호출.
  const taskSpecs = [
    { agent: "static-analyzer",  name: "정적 분석",  output: "_workspace/review/01_static.md"   },
    { agent: "design-reviewer",  name: "설계 검토",  output: "_workspace/review/02_design.md"   },
    { agent: "security-auditor", name: "보안 감사",  output: "_workspace/review/03_security.md" },
    { agent: "refactorer",       name: "리팩토링",   output: "_workspace/review/04_refactor.md",
      depends_on: ["정적 분석", "설계 검토", "보안 감사"] }
  ];
  for (const t of taskSpecs) {
    await TaskCreate({
      team: team.id,
      agent: t.agent,
      name: t.name,
      input: `_workspace/input/pr-${prNumber}.diff`,
      output: t.output,
      depends_on: t.depends_on
    });
  }

  // ──────────────────────────────────────────────
  // Phase 3 — 팬아웃 (리뷰어 3인 병렬). 동료 SendMessage는 리더 미경유.
  // ──────────────────────────────────────────────
  await waitForTeamCompletion(team.id, { tasks: ["정적 분석", "설계 검토", "보안 감사"] });
  // 워커 간 SendMessage는 워커 정의(.md)의 팀 통신 프로토콜에 따라 자율 호출.

  // ──────────────────────────────────────────────
  // Phase 4 — 생성-검증 루프 (최대 3회)
  // ──────────────────────────────────────────────
  // refactorer는 depends_on 대기 후 자동 시작. 본인이 생성·검증을 내부에서 3회 상한으로 진행.
  await waitForTeamCompletion(team.id, { tasks: ["리팩토링"] });

  // ──────────────────────────────────────────────
  // Phase 5 — 통합 · 게시 · 정리
  // ──────────────────────────────────────────────
  const reports = [
    Read("_workspace/review/01_static.md"),
    Read("_workspace/review/02_design.md"),
    Read("_workspace/review/03_security.md"),
    Read("_workspace/review/04_refactor.md")
  ];
  const merged = mergeReports(reports, { priority: ["P0", "P1", "P2"] });
  await Write("_workspace/review_report.md", merged);

  await $(`gh pr comment ${prNumber} -F _workspace/review_report.md`);
  await TeamDelete(team.id);  // workspace 보존
}
```

## 도구 분류 (책 본문 메모)

**공식 5종** (실제 호출 가능):
- TeamCreate
- AgentTool
- TaskCreate
- SendMessage (워커 정의에서 직접 호출)
- TeamDelete

**의사 함수 4종** (구현자가 직접 만들어야 함):
- `parseDiff(diff)` — diff 텍스트를 파일·라인 메타로
- `waitForTeamCompletion(teamId, opts)` — 작업 완료 대기
- `mergeReports(reports, opts)` — 4 보고서를 우선순위 정렬해 통합
- `$(cmd)` — Bash 실행 헬퍼

## 주의

- **리더 무발화**: 본 스킬은 호출만 한다. 리뷰 본문 텍스트는 워커 4인이 생산.
- **자동 커밋 금지**: 본 스킬은 `gh pr comment`까지만. `git commit`·`gh pr merge`는 호출하지 않는다.
- **workspace 보존**: TeamDelete 후에도 `_workspace/` 디렉토리는 남는다. 사람이 재검토할 수 있게.
- **재실행 트리거**: "리뷰 재실행" 키워드로 동일 prNumber 재돌리기 가능 (이전 결과 덮어쓰기).
