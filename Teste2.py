import mysql.connector
from openpyxl import Workbook
from openpyxl.styles import Font

def main():
    comando_sql = "SELECT * FROM teste2"
    dados_do_banco = executa_no_banco(comando_sql)

    dados_para_o_excel = processa_dados(dados_do_banco)
    cria_planilha(dados_para_o_excel)


def executa_no_banco(sql):
    try:
        conexao = mysql.connector.connect(host='localhost', database='infocar',user='root',password='')
        cur = conexao.cursor()
        cur.execute(sql)
        dados = cur.fetchall()
        cur.close()
        conexao.close()
        return dados

    except Exception as erro:
            print("Algo deu errado ao executar método 'executa_no_banco'\n\n",erro)
            return False

def processa_dados(dados):
    # método para deixar no máximo 30 digitos em cada célula da tabela
    try:
        dados_processados = []
        for linha in dados:
            linha_nova = []
            for celula in linha:
                if len(celula)>30:
                    linha_nova.append(celula[:30])
                else: linha_nova.append(celula)
            dados_processados.append(linha_nova)
        return dados_processados
    except Exception as e:
        print(f"Houve um erro ao processar os dados, método 'processa_dados'\n\n{e}")
        return False

def cria_planilha(dados):
    try:
        wb = Workbook()
        plan =wb.active
        plan.title = 'dados_do_banco'
        
        # Adicionando os títulos da tabela
        col=1 
        letras = ['A','B','C','D','E','F','G','H','I','J']
        for letra in letras:
            plan[f'{letra}1'] = f"col{col}"
            plan[f'{letra}1'].font = Font(bold=True)
            col+=1
        
        # Adicionando os dados resgatados do banco
        linha_excel = 2
        for linha in dados:
            col = 0
            for celula in linha:
                plan[f'{letras[col]}{linha_excel}'] = celula
                col+=1
            linha_excel +=1

        wb.save('Dados_do_banco.csv')
        print('planilha criada com sucesso')
    except Exception as e:
        print(f"Houve um erro ao criar a planilha no método 'cria_planilha'\n\n{e}")
        return False
        


if __name__ == "__main__": main()

