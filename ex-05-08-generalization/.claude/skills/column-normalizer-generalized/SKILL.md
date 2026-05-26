---
name: column-normalizer
description: "테이블 열 정규화 — 매출/금액/수량 키워드 포함 시 숫자 변환"
allowed-tools: Read, Write
---

# column-normalizer (Generalized 변형 — 책 p82)

## 규칙
- 열 이름에 "매출", "금액", "수량" 중 하나라도 포함되면 숫자로 변환한다.

(키워드 기반이라 분기·변형 열도 잡는다. 일반화. 단, 한국어 키워드만 명시됨.)
