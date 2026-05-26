---
name: sql-query
description: "데이터베이스 쿼리 생성: 매출·재고 도메인 분기. 사용자가 'Q4 매출', '재고 현황' 등을 언급하면 호출. 단순 SELECT는 직접 작성, 도메인 템플릿이 필요할 때 이 스킬을 검토."
allowed-tools: Read, Write
---

# sql-query (메뉴판 — 라우터만)

도메인 본문 없이 조건부 링크만 둔다 (메뉴판 원칙).

## 라우팅
- 매출 관련 요청이면 → `references/finance.md`
- 재고 관련 요청이면 → `references/inventory.md`

단순 SELECT는 직접 작성. 도메인 템플릿이 필요할 때만 해당 references를 로드한다.
