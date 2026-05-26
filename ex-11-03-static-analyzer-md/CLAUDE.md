# ex-11-03 — static-analyzer.md 실물

이 sub-harness는 static-analyzer 에이전트의 실물(.md)과 호출 대상 sample TS PR을 제공한다.

## 규칙
- `.claude/agents/static-analyzer.md`는 책과 동일. 임의 수정 금지.
- mock 모드 기본 — result/01_static.md는 예상 출력.
- 에이전트는 Edit·Write를 호출하지 않는다 (경계 문단).
- Bash 화이트리스트: tsc, eslint, npm run lint.
