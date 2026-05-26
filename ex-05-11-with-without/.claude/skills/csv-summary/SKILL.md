---
name: csv-summary
description: "CSV 파일 통계 요약: 행 수, 열별 dtype 추론, 숫자 열 평균·중앙값·표준편차 표 산출. 사용자가 'CSV 요약', '데이터 통계' 등을 언급하거나 .csv 파일을 첨부하면 호출."
allowed-tools: Read, Bash, Write
---

# csv-summary

CSV를 받아 통계 요약을 만든다. 실제 작동하는 미니 구현 — `bin/run.sh`가 stdlib(csv, statistics)로 요약한다.

## 사용
```
bash bin/run.sh <csv_path> <out_md>
```

## 규칙 (Why-First)
- 숫자 열만 평균/중앙값/표준편차를 낸다 — 왜냐하면 문자열 열에 통계는 의미가 없기 때문.
- 그룹 요청("부서별 평균 연봉")이면 GROUP BY 후 집계 — 왜냐하면 전체 평균은 부서 비교에 쓸 수 없기 때문.
