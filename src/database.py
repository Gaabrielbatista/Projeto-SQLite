import sqlite3

def criar_conexao():
    conn = sqlite3.connect("carros.db")
    return conn

def criar_tabela():
    conn = criar_conexao()
    cur = conn.cursor()
    
    cur.execute(
    '''CREATE TABLE IF NOT EXISTS Carros (
    id_carro INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo VARCHAR(50) NOT NULL,
    ano INTEGER NOT NULL CHECK (ano >= 1900 AND ano <= 2030),
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

# CREATE
def inserir_carro(modelo, ano, cor=None):
    modelo = modelo.strip()

    # Validações
    if not modelo:
        raise Exception("Erro: Modelo não pode estar vazio")
    if type(ano) is not int:
        raise Exception("Erro: O ano precisa ser do tipo inteiro")
    if 1900 > ano or ano > 2030:
        raise Exception("Erro: O ano precisa estar entre 1900 e 2030")

    conn = criar_conexao()
    cur = conn.cursor()

    cur.execute("INSERT INTO Carros (modelo, ano, cor) VALUES (?, ?, ?)", (modelo, ano, cor))

    conn.commit()
    conn.close()

# READ
def listar_carros():
    conn = criar_conexao()
    cur = conn.cursor()

    cur.execute("SELECT * FROM Carros")
    resultado = cur.fetchall()

    conn.close()

    return resultado

# UPDATE
def atualizar_carro(id, modelo=None, ano=None, cor=None):
    conn = criar_conexao()
    cur = conn.cursor()

    if modelo is not None:
        cur.execute("UPDATE Carros SET modelo = ? WHERE id_carro = ?", (modelo, id))
    if ano is not None:
        cur.execute("UPDATE Carros SET ano = ? WHERE id_carro = ?", (ano, id))
    if cor is not None:
        cur.execute("UPDATE Carros SET cor = ? WHERE id_carro = ?", (cor, id))

    conn.commit()
    conn.close()

# DELETE
def deletar_carro(id):
    conn = criar_conexao()
    cur = conn.cursor()

    cur.execute("DELETE FROM Carros WHERE id_carro = ?", (id, ))

    print(f"Carro na id: {id} deletado.")

    conn.commit()
    conn.close()
