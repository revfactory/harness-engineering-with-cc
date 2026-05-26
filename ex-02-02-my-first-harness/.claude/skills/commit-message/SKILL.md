---
name: commit-message
description: "스테이지된 변경을 바탕으로 Conventional Commits 형식의 커밋 메시지를 2인 팀(author·reviewer)으로 생성. '커밋 메시지', 'commit message', '커밋 메시지 만들어줘' 같은 자연어 요청 시 반드시 사용. 단, 이미 메시지가 작성된 `git commit -m` 대체는 아니다."
allowed-tools: Bash Read Write
---

# Commit Message Skill
2인 팀을 순차로 호출해 Conventional Commits 형식의 커밋 메시지를 생성한다.

## Workflow
1. Precondition 체크.
   `git diff --cached --quiet` 를 실행한다.
   exit code 1(변경 있음)이면 통과, exit code 0(변경 없음)이면 "먼저 `git add`" 안내 후 종료.
2. author 호출.
   `commit-msg-author` 에이전트를 Agent 도구로 호출.
   출력은 `_workspace/commit-draft.md`.
3. reviewer 호출.
   `commit-msg-reviewer` 에이전트를 Agent 도구로 호출.
   출력은 `_workspace/review-report.md`.
4. 판정 분기.
   - PASS. `_workspace/commit-draft.md` 내용을 사용자에게 제시하고 완료.
   - REDO. reviewer 수정 지시를 프롬프트에 포함해 author 재호출 (최대 2회).
5. 루프 종료.
   PASS 또는 재호출 2회 초과 시 종료.
   초과 시 "자동 승인 한계 도달 — 수동 검토 권장" 경고와 함께 마지막 draft 반환.

