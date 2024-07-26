import sqlite3
import pandas as pd

#CREAMOS LA CONECCIÓN A LA BD
conn = sqlite3.connect('ecommerce.db')

#CREAMOS EL DF
df1=pd.read_csv('D:/Data Engineer/TP-1-Parte-3/TP-1-Parte-3/ecommerce_customers_dataset.csv',encoding='utf-8')
df2=pd.read_csv('D:/Data Engineer/TP-1-Parte-3/TP-1-Parte-3/ecommerce_order_items_dataset.csv',encoding='utf-8')
df3=pd.read_csv('D:/Data Engineer/TP-1-Parte-3/TP-1-Parte-3/ecommerce_order_payments_dataset.csv',encoding='utf-8')
df4=pd.read_csv('D:/Data Engineer/TP-1-Parte-3/TP-1-Parte-3/ecommerce_orders_dataset.csv',encoding='utf-8')
df5=pd.read_csv('D:/Data Engineer/TP-1-Parte-3/TP-1-Parte-3/ecommerce_products_dataset.csv',encoding='utf-8')

#ESTABLECE LA COLUMNA INDICE
df1.set_index('customer_id', inplace=True)
df2.set_index('order_id', inplace=True)
df3.set_index('order_id', inplace=True)
df4.set_index('order_id', inplace=True)
df5.set_index('product_id', inplace=True)


#GUARDAMOS EL DF EN UNA TABLA
df1.to_sql('customers', conn, if_exists='replace', index=True, index_label='customer_id')
df2.to_sql('order_items', conn, if_exists='replace', index=True, index_label='order_id')
df3.to_sql('order_payment', conn, if_exists='replace', index=True, index_label='order_id')
df4.to_sql('orders', conn, if_exists='replace', index=True, index_label='order_id')
df5.to_sql('products', conn, if_exists='replace', index=True, index_label='product_id')

# CREAMOS UN CURSOR PARA ESTABLECER LA PK
# cursor = conn.cursor()
# cursor.execute("ALTER TABLE customers ADD PRIMARY KEY (customer_id)")
# conn.commit


#CERRAMOS LA CONEXIÓN A LA BD
conn.close()