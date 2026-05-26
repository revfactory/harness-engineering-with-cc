# sample-app — 의도적 취약 Flask 앱 (데모 전용)

> **경고: 절대 배포하지 말 것.** security-analyst 에이전트의 분석 대상으로만
> 쓰는 의도적 취약 코드다.

## 심어둔 취약점 (정답지)

| # | 취약점 | 위치 | OWASP |
|---|--------|------|-------|
| 1 | SQL Injection (문자열 포매팅) | app.py login/register/get_user | A03:2021 |
| 2 | 하드코딩 자격증명(SECRET_KEY, DB_PASSWORD) | app.py 13-15 | A05/A07:2021 |
| 3 | 약한 해시(MD5)로 비밀번호 저장 | app.py register | A02:2021 |
| 4 | XSS(이스케이프 없는 HTML 렌더링) | app.py profile | A03:2021 |
| 5 | IDOR / 인가 누락(`/api/users/<id>`) | app.py get_user | A01:2021 |
| (보너스) | debug=True 운영 노출 | app.py main | A05:2021 |
