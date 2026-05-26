# ex-11-06 JWT PR + 의도 버그 4종 + 4인 팀 실행 (mock)

> 의도된 버그 4종(SQL 인젝션·N+1·경계면 불일치·테스트 0건)이 심긴 JWT 리프레시 PR + mock 4 리뷰어 산출 + Without/With 비교.

## 모드

- **mock (기본)**: 실 Claude Code 호출 0. 산출은 예상 출력.
- **live (옵션, 본 환경에서는 미실행)**: 환경 변수 `EX_11_06_MODE=live`로만 실 4 에이전트 호출. 입력 prompt 5k token 상한, 출력 5k.

## PR 통계
- 파일: 5 (refresh.ts / users.ts / useUser.ts / schema.prisma / jwt.ts)
- 총 라인: 296 (약 300줄)
- INTENT_BUG 마커: 4종, grep 카운트 8 (마커 + 짝 메모)

## 핵심 산출
- `fixtures/sample-pr-jwt/` — PR 실물 5파일
- `result/discovery-matrix.md` — 4 × 4 발견 매트릭스
- `result/without-team.md` — Without 1인 시뮬레이션
- `result/compare-table.md` — 6행 비교
- `result/cross-domain-log.md` — SendMessage 6건
- `result/observation-notes.md` — 책 vs 실측

## 검증
```bash
grep -rn "INTENT_BUG_" fixtures/sample-pr-jwt/src fixtures/sample-pr-jwt/prisma
# 8 매치 (4 버그 × 마커+메모)
```
