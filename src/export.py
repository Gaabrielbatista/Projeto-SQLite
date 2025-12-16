import csv
from database import criar_conexao
from datetime import datetime

# data hoje:
hoje = datetime.now().today()

def exportar_csv():
    # Conectar ao banco de dados e buscar os dados
    conn = criar_conexao()
    cur = conn.cursor()
    
    with open(f'exports/export_carros_{hoje.strftime("%d-%m-%Y")}.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        # Escrever o cabeçalho
        escritor_csv.writerow(['ID', 'Modelo', 'Ano', 'Cor'])
        
        cur.execute("SELECT * FROM Carros")
        dados_carros = cur.fetchall()
        
        # Escrever os dados no arquivo CSV
        for carro in dados_carros:
            escritor_csv.writerow(carro)

        conn.close()
