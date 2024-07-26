import sqlite3
import pandas as pd

#CREAMOS LA CONECCIÓN A LA BD
conn = sqlite3.connect('ecommerce.db')

#CREAMOS EL DF
df1=pd.read_csv('D:/Data Engineer/TP-1-Parte-3/ecommerce_customers_dataset.csv',encoding='utf-8')


#GUARDAMOS EL DF EN UNA TABLA
df1.to_sql('customers',conn, if_exists='replace',index=True, index_label='customer_id')


#CERRAMOS LA CONEXIÓN A LA BD
conn.close()