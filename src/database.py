import sqlite3
from utils import validar_dados_carro, verificar_id_existe

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
    # Validação
    dados_carro = validar_dados_carro(modelo, ano, cor)

    if not dados_carro[0]:
        raise Exception("Erro: Modelo não pode estar vazio.")
    
    # Inserção
    conn = criar_conexao()
    cur = conn.cursor()

    cur.execute("INSERT INTO Carros (modelo, ano, cor) VALUES (?, ?, ?)", dados_carro)

    print("Carro criado!")
    conn.commit()
    conn.close()

# READ
def listar_carros(ano=0):
    conn = criar_conexao()
    cur = conn.cursor()

    if ano > 0:
        cur.execute("SELECT * FROM Carros WHERE ano >= ?", (ano,))
    elif ano < 0:
        cur.execute("SELECT * FROM Carros WHERE ano <= ?", (abs(ano),))
    else:
        cur.execute("SELECT * FROM Carros")

    resultado = cur.fetchall()

    conn.close()

    return resultado

# UPDATE
def atualizar_carro(id, modelo=None, ano=None, cor=None):
    verificar_id_existe(id)

    modelo_carro, ano_carro, cor_carro = validar_dados_carro(modelo, ano, cor)
    conn = criar_conexao()
    cur = conn.cursor()

    if isinstance(modelo_carro, str) and modelo_carro.strip() == "":
        raise Exception("Erro: Modelo se encontra vazio")
    if modelo_carro is not None and (not isinstance(modelo_carro, str) or modelo_carro.strip() != ""):
        cur.execute("UPDATE Carros SET modelo = ? WHERE id_carro = ?", (modelo_carro, id))

    if ano_carro is not None:
        cur.execute("UPDATE Carros SET ano = ? WHERE id_carro = ?", (ano_carro, id))

    if isinstance(cor_carro, str) and cor_carro.strip() == "":
        raise Exception("Erro: Cor se encontra vazio")
    if cor_carro is not None and (not isinstance(cor_carro, str) or cor_carro.strip() != ""):
        cur.execute("UPDATE Carros SET cor = ? WHERE id_carro = ?", (cor_carro, id))

    print(f"Carro no ID: {id} atualizado!")

    conn.commit()
    conn.close()

# DELETE
def deletar_carro(id):
    verificar_id_existe(id)

    conn = criar_conexao()
    cur = conn.cursor()

    cur.execute("DELETE FROM Carros WHERE id_carro = ?", (id, ))

    print(f"Carro no ID: {id} deletado!")

    conn.commit()
    conn.close()
