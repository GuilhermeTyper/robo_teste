import datetime
import pandas as pd

#Simulação de coleta de dados
def coletar_dados():
    return [
        {"data" : datetime.date.today(), "evento": "Processamento Finalizado","Status": "OK"}
    ]

#Salvar em um CSV
def salvar_em_csv(dados):
    df = pd.DataFrame(dados)
    df.to_csv('dados/relatorio.csv', index=False)
    print(f"Relatório salvo com Sucesso!")

    #Execução Principal

    if __name__ == "__main__":
        print('Iniciando ROBO...')
        dados = coletar_dados()
        salvar_em_csv(dados)