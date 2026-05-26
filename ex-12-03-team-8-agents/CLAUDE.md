# ex-12-03 CLAUDE.md

본 sub-harness는 8 에이전트 정의 모음.

**물리적 강제 사항:**
- `boundary-verifier`는 `tools`에 **Edit 미포함**. "verifier의 역할은 문제 검증이지 수정이 아니다" 원칙을 frontmatter로 강제.
- `test-suite`는 PM 단독 수신 — SendMessage 도구 미부여.
- 설계 3종(api-designer / ui-designer / db-migrator)은 model=opus, tools에 Edit 미포함 (설계만).
- 구현 2종(backend-impl / frontend-impl)은 model=sonnet, tools에 Edit·Bash 포함.

**팀 규모 원칙:**
> 세션당 한 팀, Phase당 3~4개의 에이전트를 유지하는 게 좋습니다.

본 팀은 총 8명이지만, Phase별 동시 활성은 최대 4명. `01_phase_matrix.md`로 강제.

**금지:**
- 본 디렉토리에서 `.claude/agents/` 외 다른 에이전트 추가 금지.
- 8 에이전트의 frontmatter 4 필수키(name / description / model / tools) 누락 금지.
