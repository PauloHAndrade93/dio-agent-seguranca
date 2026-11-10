"""
app_corrigido.py  -  Versao SEGURA do login (uso de laboratorio)

Corrige a falha de SQL Injection do 'app.py' usando CONSULTA PARAMETRIZADA:
a entrada do usuario vai como parametro (?), nunca concatenada na string SQL.
O driver do banco trata os valores como dados, nao como codigo.

Esta e a mitigacao recomendada para CWE-89 (SQL Injection).
"""

import sqlite3


def criar_banco_demo():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, usuario TEXT, senha TEXT)")
    cur.execute("INSERT INTO usuarios (usuario, senha) VALUES ('admin', 's3nh4_forte')")
    conn.commit()
    return conn


def login(conn, usuario, senha):
    """
    SEGURO: usa placeholders (?) e passa a entrada como parametros.
    A mesma entrada maliciosa que burlava o app.py aqui nao tem efeito,
    porque o banco nunca interpreta os valores como SQL.
    """
    cur = conn.cursor()
    query = "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?"
    cur.execute(query, (usuario, senha))
    return cur.fetchone() is not None


if __name__ == "__main__":
    conn = criar_banco_demo()

    print("== Login legitimo ==")
    print("Acesso:", login(conn, "admin", "s3nh4_forte"))

    print("\n== Tentativa com credencial errada ==")
    print("Acesso:", login(conn, "admin", "errada"))

    print("\n== Mesma entrada maliciosa de antes (agora sem efeito) ==")
    print("Acesso:", login(conn, "' OR '1'='1' --", "qualquer"))
