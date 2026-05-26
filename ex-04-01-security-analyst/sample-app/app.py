# sample-app — 의도적 취약 Flask 앱 (데모 전용, 배포 금지)
# 각 취약점에 OWASP Top 10 식별자를 주석으로 표기.
import hashlib
from flask import Flask, request, render_template_string
from db import get_connection

app = Flask(__name__)

# OWASP A05:2021 (Security Misconfiguration) / A07 — 하드코딩 자격증명
SECRET_KEY = "admin1234"          # 평문 시크릿 키 하드코딩
DB_PASSWORD = "root_password_123"  # DB 비밀번호 코드 내 평문
app.secret_key = SECRET_KEY


@app.route("/login")
def login():
    name = request.args.get("name", "")
    conn = get_connection(DB_PASSWORD)
    cur = conn.cursor()
    # OWASP A03:2021 (Injection) — SQL Injection: 사용자 입력 문자열 포매팅
    query = f"SELECT * FROM users WHERE name = '{name}'"
    cur.execute(query)
    row = cur.fetchone()
    return {"user": row}


@app.route("/register")
def register():
    name = request.args.get("name", "")
    pw = request.args.get("pw", "")
    # OWASP A02:2021 (Cryptographic Failures) — 약한 해시(MD5)로 비밀번호 저장
    pw_hash = hashlib.md5(pw.encode()).hexdigest()
    conn = get_connection(DB_PASSWORD)
    conn.cursor().execute(
        f"INSERT INTO users (name, pw) VALUES ('{name}', '{pw_hash}')"
    )
    conn.commit()
    return {"status": "ok"}


@app.route("/profile")
def profile():
    bio = request.args.get("bio", "")
    # OWASP A03:2021 (XSS) — 사용자 입력을 이스케이프 없이 HTML 렌더링
    tmpl = "<html><body><h1>Profile</h1><p>" + bio + "</p></body></html>"
    return render_template_string(tmpl)  # autoescape 우회: 문자열 직접 결합


@app.route("/api/users/<int:user_id>")
def get_user(user_id):
    # OWASP A01:2021 (Broken Access Control / IDOR) — 본인 확인 없이 임의 ID 접근
    conn = get_connection(DB_PASSWORD)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return {"user": cur.fetchone()}


if __name__ == "__main__":
    # OWASP A05:2021 — 운영에서 debug=True (스택트레이스 노출)
    app.run(debug=True, host="0.0.0.0")
