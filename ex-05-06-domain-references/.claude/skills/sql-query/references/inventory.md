# 재고 쿼리 템플릿 (레시피 — 재고 요청 시만 로드)

> 합성 더미. 민감 정보 없음.

## 1. 재고 현황
```sql
SELECT sku, on_hand FROM inventory ORDER BY sku;
```

## 2. 부족 알림
```sql
SELECT sku, on_hand, safety_stock
FROM inventory WHERE on_hand < safety_stock;
```

## 3. 회전율
```sql
SELECT sku, shipped_qty * 1.0 / NULLIF(avg_stock, 0) AS turnover
FROM inventory_stats;
```
