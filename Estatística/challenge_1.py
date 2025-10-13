# Challenge 1: Tratamento da base de dados Tourism Experience
#pip install openpyxl

import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('C:/Users/cyamauchi/Documents/FIAP/Nova pasta/tourism_dataset.csv') #Importar a base original do kaggle e o código irá tratá-la para a base final

df_limpo = df.drop(columns=['Review_Sentiment','Recommendation_Score'])
df_agg = df_limpo.groupby(['Location_Type', 'Season', 'Duration', 'Budget','Travel_Group_Size']).agg(
  total_reviews = ('User_ID', 'count'),
  avg_user_rating = ('User_Rating', 'mean'),
  avg_spending_per_day = ('Avg_Spending_per_day', 'mean'),
).reset_index()
print("Dataframe tratado:\n")
print(df_agg)

#Exportar para excel
df_agg.to_excel('C:/Users/cyamauchi/Documents/FIAP/Nova pasta/Base_dados_Tourism_Experience.xlsx', index=False)

'''
2. Tabela de Distribuição de Frequências

 a) 1 variável quantitativa discreta, na sequência, extraia pelo menos 2 insights da tabela utilizando #. 

 b) 1 variável quantitativa contínua, na sequência, extraia pelo menos 2 insights da tabela utilizando #.
'''

#Tabela de distribuição de frequências pelo tamanho do grupo de viagem pela quantidade de reviews
print('---------------------------------------------------------------------------------------------------------------------------------------')
df_dist_freq = df_agg.groupby(['Travel_Group_Size'])['total_reviews'].sum().reset_index().sort_values(by='total_reviews',ascending=False)
df_dist_freq.rename(columns={'total_reviews': 'Frequência Absoluta (Fi)'}, inplace=True)
total_geral = df_dist_freq['Frequência Absoluta (Fi)'].sum()
df_dist_freq['Frequência Relativa (Fr %)'] = (df_dist_freq['Frequência Absoluta (Fi)'] / total_geral * 100).round(2)
df_ordenado = df_dist_freq.sort_values(by='Frequência Absoluta (Fi)', ascending=False)
df_ordenado['Frequência Acumulada (Fac)'] = df_ordenado['Frequência Absoluta (Fi)'].cumsum()
print("\nTabela de distribuição de frequências pelo tamanho do grupo de viagem pela quantidade de reviews:\n")
print(df_ordenado.to_string(index=False))
# Insights
print("\nInsights:")
print("# A maior frequência de reviews está em grupos de 5 pessoas.")
print("# As faixas variam pouco entre si, o que pode indicar um tratamento prévio dos dados para ter grupos estatísticamente comparáveis.\n")

#Tabela de distribuição de frequências pelo tempo médio de gasto por dia pela quantidade de reviews

limites = [100, 200, 300, 400, 500, 600] 
rotulos = ['100 a 200', '200 a 300', '300 a 400','400 a 500', '500 a 600'] 

df_agg['Faixa de tempo'] = pd.cut(x=df_agg['avg_spending_per_day'],
                              bins=limites,
                              labels=rotulos,
                              include_lowest=True, 
                              right=True) 

df_spending_per_day = df_agg.groupby('Faixa de tempo', observed=True)['total_reviews'].sum().reset_index()
df_spending_per_day.rename(columns={'total_reviews': 'Frequência Absoluta (Fi)'}, inplace=True)
total_geral = df_spending_per_day['Frequência Absoluta (Fi)'].sum()
df_spending_per_day['Frequência Relativa (Fr %)'] = (df_spending_per_day['Frequência Absoluta (Fi)'] / total_geral * 100).round(2)
df_spending_per_day['Frequência Acumulada (Fac)'] = df_spending_per_day['Frequência Absoluta (Fi)'].cumsum()
print('---------------------------------------------------------------------------------------------------------------------------------------')

print("\nTabela de distribuição de frequências pelo tempo médio de gasto por dia pela quantidade de reviews:\n")
print(df_spending_per_day.to_string(index=False))

# Insights
print("\nInsights:")
print("# A maior frequência de reviews está na faixa de gasto de 100 a 200 por dia.")
print("# As faixas de gasto acima de 300 por dia representam uma menor proporção de reviews.")

print('---------------------------------------------------------------------------------------------------------------------------------------')