# ex-11-05 — code-review-team 오케스트레이터

## 하네스: 코드 리뷰 자동화

이 디렉토리는 4 에이전트(static-analyzer / design-reviewer / security-auditor / refactorer) + 1 스킬(code-review-team)로 PR 리뷰를 수행한다.

## 트리거 키워드
- "코드 리뷰", "PR 리뷰", "리뷰 재실행", "다시 실행"
- 위 키워드는 `code-review-team` 스킬에 라우팅

## 규칙
- 리더는 텍스트 무발화 (호출만)
- 자동 커밋 금지 (git commit 0건)
- workspace 보존 (TeamDelete 후에도 _workspace/ 잔존)
- refactorer 생성-검증 루프 ≤ 3회
