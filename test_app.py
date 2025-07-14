import psycopg2

def test_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="testdb",
        user="testuser",
        password="testpass"
    )
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    result = cur.fetchone()
    assert result[0] == 1
    conn.close()
