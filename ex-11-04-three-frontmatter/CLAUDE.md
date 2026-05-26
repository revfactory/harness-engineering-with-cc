# ex-11-04 — 3 에이전트 실물 + 4인 팀 공존

이 sub-harness는 security/design/refactor 3 에이전트 실물을 보유한다. static-analyzer는 ex-11-03에서 복사.

## 규칙
- 프론트매터 임의 수정 금지 (책과 일치)
- design-reviewer는 **Bash 없음** — 텍스트만 읽음
- refactorer Edit 대상은 `_workspace/patches/*.diff`만 — 소스 직접 수정 금지
- 자동 커밋 금지: 누구도 git 호출하지 않는다
