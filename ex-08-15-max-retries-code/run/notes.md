# 책 인용 · 검증 메모

## 책 p140 인용

> MAX_RETRIES = 3을 두어 무한 루프를 차단한다. 3회 안에 PASS가 안 나면 `f"escalated: {MAX_RETRIES}회 실패, 수동 개입 필요"`를 반환하고 사람에게 넘긴다.

## 시그니처 보존 체크

- [x] `MAX_RETRIES = 3` (모듈 상수)
- [x] `for attempt in range(MAX_RETRIES):`
- [x] `if result.passed: return artifact`
- [x] 루프 탈출 후 `f"escalated: {MAX_RETRIES}회 실패, 수동 개입 필요"` 반환
- [x] Python3 표준 라이브러리만 (dataclass, sys)

## 책에 없는 보완

- 더미 `CodeGenerator`·`TestRunner` 클래스 — 실행 가능성 확보용.
- CLI 인자 `success`/`fail`로 두 시나리오 분기.
- attempt별 print로 진행 추적 — 디버깅 가시성.

## 본 빌드 상태

- **코드 미실행**: 빌드 가이드("스크립트/네트워크 실행 금지")에 따라 정적 분석으로 예상 출력 도출.
- 사용자가 직접 실행할 경우: `python3 run/max_retries.py success` 또는 `python3 run/max_retries.py fail`.

## Cross-link

- 다이어그램: **ex-08-13**
- 트레이드오프(무한 루프 단점): **ex-08-16**
- 안티패턴 #2 (무한 재시도): **ex-08-33**
