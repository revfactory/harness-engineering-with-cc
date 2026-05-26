# ex-05-11 — With/Without 스킬 비교 1사이클

csv-summary 스킬 1건에 With/Without를 동시 실행(`&`+`wait`)해 pass_rate·duration_ms·total_tokens 3축 비교 + 변별력 있는/없는 단언 반례까지 산출 (synthesize).

## 실행
`bash result/bin/run-both.sh` → with/without output·metrics·grading 생성, comparison.md 갱신.

## 보기
`.claude/skills/csv-summary/{SKILL.md,bin/run.sh}`, `fixtures/{prompt.md,sample.csv}`, `result/{comparison.md,non-discriminating-demo.md}`.
total_tokens는 추정치(stub) — analysis 메모 참조.
