# 매출 쿼리 템플릿 (레시피 — 매출 요청 시만 로드)

> 합성 더미. 민감 정보 없음.

## 1. 일별 매출
```sql
SELECT sale_date, SUM(amount) AS daily_revenue
FROM sales GROUP BY sale_date ORDER BY sale_date;
```

## 2. 카테고리별 매출
```sql
SELECT category, SUM(amount) AS revenue
FROM sales GROUP BY category ORDER BY revenue DESC;
```

## 3. YoY 비교
```sql
SELECT EXTRACT(YEAR FROM sale_date) AS yr, SUM(amount) AS revenue
FROM sales GROUP BY yr ORDER BY yr;
```
