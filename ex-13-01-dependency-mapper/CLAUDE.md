# ex-13-04 CLAUDE.md

- `.claude/agents/dependency-mapper.md`는 책 원본 그대로. tools는 정확히 `Read, Grep, Bash`. Write/Edit 절대 추가 금지.
- 절차 6단계 어휘를 한 글자도 변경하지 않는다.
- 본 예제는 mock 모드(USE_LIVE_LLM 미설정 = 기본)로 실행한다. mock-mapper.sh가 결정론적 batches.json을 산출.
- 실제 sonnet 호출은 `USE_LIVE_LLM=1` 환경변수에서만 (이 빌드에서는 실행하지 않음).
