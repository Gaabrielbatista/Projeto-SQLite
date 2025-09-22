import sqlite3

def criar_conexao():
    conn = sqlite3.connect("carros.db")
    return conn

def criar_tabela():
    conn = criar_conexao()
    cur = conn.cursor()
    
    cur.execute(
    '''CREATE TABLE IF NOT EXISTS carros (
    id_carro INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo VARCHAR(50) NOT NULL,
    ano INTEGER NOT NULL CHECK (ano >= 1900 AND ano < 2030),
    cor VARCHAR(30)
    );''')
    
    conn.commit()
    conn.close()

def listar_tabelas():
    conn = criar_conexao()
    cur = conn.cursor()

    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

    resultado = cur.fetchall()
    conn.close()

    return resultado

def inserir_carro(modelo, ano, cor):
    conn = criar_conexao()
    cur = conn.cursor()

    cur.execute("INSERT INTO carros (modelo, ano, cor) VALUES (?, ?, ?)", (modelo, ano, cor))

    conn.commit()
    conn.close()

def listar_carros():
    conn = criar_conexao()
    cur = conn.cursor()

    cur.execute("SELECT * FROM carros")
    resultado = cur.fetchall()
    conn.close()
    return resultado
