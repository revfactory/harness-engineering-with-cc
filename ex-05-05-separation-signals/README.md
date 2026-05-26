# ex-05-05 — 분리 신호 진단

책 3신호 표(크기·도메인 분기·조건부 상세)를 옮기고, skill-size-auditor가 3개 샘플 SKILL.md를 진단해 신호 발현을 정확히 잡는지 검증 (extend).

## 보기
`result/signals-table.md`, `fixtures/samples/{size,domain,conditional}/SKILL.md`, `.claude/agents/skill-size-auditor.md`, `result/diagnosis/*.md`, `result/after/.../sample/`(분리 후), `result/diff-summary.md`.
진단은 dry-run: wc/grep는 실제 실행, LLM 판정은 설계 명세대로 예상 결과 기록.
