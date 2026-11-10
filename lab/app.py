"""
app.py  -  CODIGO PROPOSITALMENTE VULNERAVEL (uso de laboratorio)

Exemplo de login inseguro usado para testar a skill 'vulnerability-analysis'
do DIO Agent. A funcao de login monta o SQL concatenando o que a pessoa
digitou, o que abre uma falha de SQL Injection (CWE-89).

NAO use este padrao em producao. A versao corrigida esta em 'app_corrigido.py'.
Rode apenas no seu ambiente de laboratorio, com um banco de teste.
"""

import sqlite3


def criar_banco_demo():
    """Cria um banco de teste em memoria com um usuario de exemplo."""
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, usuario TEXT, senha TEXT)")
    cur.execute("INSERT INTO usuarios (usuario, senha) VALUES ('admin', 's3nh4_forte')")
    conn.commit()
    return conn


def login(conn, usuario, senha):
    """
    VULNERAVEL: monta a query concatenando a entrada do usuario direto na
    string SQL. Uma entrada como  usuario = "' OR '1'='1' --"  burla o login.
    """
    cur = conn.cursor()
    query = (
        "SELECT * FROM usuarios "
        "WHERE usuario = '" + usuario + "' AND senha = '" + senha + "'"
    )
    print(f"[SQL executado] {query}")
    cur.execute(query)
    return cur.fetchone() is not None


if __name__ == "__main__":
    conn = criar_banco_demo()

    print("== Login legitimo ==")
    print("Acesso:", login(conn, "admin", "s3nh4_forte"))

    print("\n== Tentativa com credencial errada ==")
    print("Acesso:", login(conn, "admin", "errada"))

    print("\n== Entrada maliciosa (demonstra a falha) ==")
    # Classico bypass de autenticacao via SQL Injection
    print("Acesso:", login(conn, "' OR '1'='1' --", "qualquer"))
