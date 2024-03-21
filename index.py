import pandas as pd
import matplotlib.pyplot as plt

# Armazenamos as planilhas nas variáveis
arquivoExcel1 = 'vendas.xlsx'
arquivoExcel2 = 'vendedores.xlsx'

# Usamos o Pandas para ler os arquivos das planilhas e mencionamos o sheet_name (a aba)
df_vendas = pd.read_excel(arquivoExcel1, sheet_name='Planilha1')
df_vendasProduto = pd.read_excel(arquivoExcel1, sheet_name='Planilha2')
df_vendedores = pd.read_excel(arquivoExcel2)

# Unimos os dados em um só
df_todas_as_planilhas = pd.concat([df_vendas, df_vendasProduto, df_vendedores])

# Verificar as frutas mais vendidas

## Selecionamos apenas duas colunas da planilha
frutas_e_Qtd = ['Produto', 'Quantidade']
df_Frutas = df_vendas[frutas_e_Qtd]

## Achamos o id da maior quantidade na linha
indice_maior_quantidade = df_Frutas['Quantidade'].idxmax()

## Localizamos esse id na planilha unificada e achamos o id na coluna 'Produto'
fruta_mais_vendida = df_Frutas.loc[indice_maior_quantidade, 'Produto']

# Plotar o gráfico de barras
plt.bar(df_Frutas['Produto'], df_Frutas['Quantidade'], color='skyblue')

# Destacar a fruta mais vendida
plt.bar(df_Frutas.loc[indice_maior_quantidade, 'Produto'],
        df_Frutas.loc[indice_maior_quantidade, 'Quantidade'],
        color='orange', label='Maior Quantidade')
plt.ylabel('Quantidade')
plt.show()

# Printamos
##print(df_Frutas)
