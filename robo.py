import datetime
import pandas as pd

# Simula coleta de dados
def coletar_dados():
    return [
        {"data": datetime.date.today(), "evento": "Processamento finalizado", "status": "OK"},
    ]

# Salva os dados em um CSV
def salvar_relatorio(dados):
    df = pd.DataFrame(dados)
    df.to_csv('dados/relatorio.csv', index=False)
    print("✅ Relatório salvo com sucesso!")

# Execução principal
if __name__ == "__main__":
    print("🤖 Iniciando robô...")
    dados = coletar_dados()
    salvar_relatorio(dados)

