# sample-app/db.py — 데모용 DB 헬퍼 (의도적 취약)
import sqlite3

# OWASP A05:2021 — 연결 비밀번호를 인자로 받지만 검증·암호화 없음(데모)
def get_connection(password):
    # 데모: 실제로는 sqlite 파일. password는 무시(평문 전달 시연용).
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection("ignored")
    conn.execute(
        "CREATE TABLE IF NOT EXISTS users ("
        "id INTEGER PRIMARY KEY, name TEXT, pw TEXT)"
    )
    conn.commit()
