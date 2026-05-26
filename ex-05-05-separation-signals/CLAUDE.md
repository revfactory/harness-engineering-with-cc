# CLAUDE.md — ex-05-05 분리 신호 진단

- 3신호 표는 책 그대로 보존한다.
- 샘플 3건은 각각 의도한 신호를 발현해야 한다: size >= 500줄, domain은 분기 키워드 >= 2개, conditional은 "~이면 -> 참조" 패턴 >= 1개.
- skill-size-auditor 진단은 3건 모두 정확해야 한다 (false positive/negative 0).
- 분리 후 SKILL.md는 도메인 분기 본문을 내포하지 않고 references로 위임한다.
- 진단의 LLM 판정 부분은 dry-run 예상치 — wc -l/grep 기반 수치는 실제 실행값.
