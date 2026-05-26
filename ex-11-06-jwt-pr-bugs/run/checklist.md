# 셀프 체크 (ex-11-06)

- [x] sample-pr-jwt 5파일 작성 (총 296줄, 약 300줄 목표)
- [x] INTENT_BUG_ 마커 4종 모두 grep 가능 (BUG_1·2·3·4)
  - BUG_1: SQL 인젝션 (users.ts:41-42)
  - BUG_2: N+1 쿼리 (users.ts:53-58)
  - BUG_3: 경계면 불일치 (refresh.ts:50 + useUser.ts:45)
  - BUG_4: 테스트 0건 (refresh.ts:60 주석)
- [x] 4 리뷰어 mock 보고서 (01~04) 작성
- [x] 발견 매트릭스 4×4 (책 양식 일치)
- [x] 버그 2 (N+1) — 3 에이전트 모두 발견 (cross-domain 증거)
- [x] cross-domain-log.md SendMessage ≥1건 (실제 6건)
- [x] Without 팀 시뮬레이션 → 2/4
- [x] compare-table.md 6행, mock에서 토큰·비용 "측정 안 됨" 표기
- [x] observation-notes.md 책 vs 실측 차이 메모
- [x] "추정값" 면책 보존
- [x] mock 모드 기본, EX_11_06_MODE=live 환경변수 명세
