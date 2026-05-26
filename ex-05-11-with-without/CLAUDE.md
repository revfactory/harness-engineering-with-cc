# CLAUDE.md — ex-05-11 With/Without 비교

- With/Without은 동시 실행(`&` 백그라운드 + `wait`)한다 (F1: 순차 시 캐시·파일 오염).
- 같은 프롬프트 / 다른 스킬 구성 / 다른 출력 경로 — 3조건 (F2).
- 단언 >= 1건은 변별력 있어야 한다 (with PASS / without FAIL, F4).
- 변별력 없는 단언("출력 존재")은 두 환경 모두 PASS -> "non-discriminating" 라벨 (F3).
- 비교 표 컬럼 = pass_rate / duration_ms / total_tokens (F5: 품질·속도·비용 3축).
- total_tokens는 실제 API 사용 시만 정확 — stub 환경에선 "estimated" 라벨 + 추정 방식 기록.
- 책 표 수치(0.83, 18,500 등)는 저자 실측 — 본 수치와 동일하지 않을 수 있음 (정량 일치가 아니라 방법론 일치가 본질).
