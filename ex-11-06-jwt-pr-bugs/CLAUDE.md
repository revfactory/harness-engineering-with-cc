# ex-11-06 — JWT PR 4인 팀 실행

## 모드 결정

| 환경변수 | 동작 |
|---------|------|
| `EX_11_06_MODE=mock` (기본) | result/는 예상 출력. 실 호출 0. |
| `EX_11_06_MODE=live` | 실 4 에이전트 호출. 본 환경에서는 **미실행**. |

## live 모드 안전 조치
- 입력 prompt 5k token 상한
- 출력 5k token 상한
- Bash는 sample-pr-jwt 내부에서만
- 자동 커밋 금지 (refactorer git commit 호출 0건)
- gh pr comment는 dry-run echo

## 의도된 버그 위치 (grep 검증용)
```
INTENT_BUG_1  src/api/users.ts:41-42      SQL 인젝션
INTENT_BUG_2  src/api/users.ts:53-58      N+1 쿼리
INTENT_BUG_3  src/api/auth/refresh.ts:50  응답 형식 — 객체
              src/hooks/useUser.ts:45     응답 형식 — 배열 기대 (짝)
INTENT_BUG_4  src/api/auth/refresh.ts:60  refresh.test.ts 부재
```
