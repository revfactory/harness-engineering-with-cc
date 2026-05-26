# CLAUDE.md — ex-05-12 안티패턴 진단

- 3안티패턴 표는 책 그대로 보존한다 (내용·문제점·해결).
- 위반 샘플 3건은 각각 의도한 안티패턴을 명백히 발현: ap1 wc -l >= 500, ap2 references/ 부재 + 본문 분기 >= 4, ap3 ALWAYS/NEVER/반드시/절대 >= 5 & 왜냐하면/때문에 = 0.
- antipattern-detector 진단은 3건 모두 정확 (false positive 0).
- 각 진단에 심각도(low/med/high) 등급.
- cross-ref: 안티패턴1 <-> Progressive Disclosure, 2 <-> Layer3 누락, 3 <-> Why-First.
- wc/grep 수치는 실측, LLM 판정은 dry-run 예상치.
