# ex-05-08 — 일반화 vs 오버피팅 재적용 실측

책 Overfit/Generalized SKILL.md 2개로 7건 테스트 열에 N=3 반복 적용해 적용률을 비교 (extend).

## 보기
`.claude/skills/column-normalizer-{overfit,generalized}/SKILL.md`(책 그대로), `fixtures/test-columns.md`(7건), `result/results.csv`(42행, dry-run 예상치), `result/analysis.md`.
실측 미수행(dry-run): rule-applicator LLM 호출 대신 설계 명세대로 예상 판정 기록.
