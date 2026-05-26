# CLAUDE.md — ex-05-08 일반화 vs 오버피팅

- Overfit/Generalized 본문은 책 글자 그대로 옮긴다.
- rule-applicator는 본문 1개 + 테스트 열 이름 1건 -> "숫자 변환 yes/no" + 사유.
- 본 빌드는 dry-run: 실제 LLM 호출 없이 설계 명세대로 예상 판정 기록.
- C5(영어 키워드 "Total Amount")를 Generalized가 못 잡으면, "한국어 키워드만 명시"라는 한계로 관찰 메모에 기록 (책에 보완 제안). 결과를 책에 맞추지 않는다.
- C7("상품명") 부정 케이스는 두 변형 모두 거부해야 한다.
