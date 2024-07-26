import pandas as pd 

df1=pd.read_csv('D:/Data Engineer/TP-1-Parte-3/TP-1-Parte-3/ecommerce_customers_dataset.csv',encoding='utf-8')
df2=pd.read_csv('D:/Data Engineer/TP-1-Parte-3/TP-1-Parte-3/ecommerce_order_items_dataset.csv',encoding='utf-8')
df3=pd.read_csv('D:/Data Engineer/TP-1-Parte-3/TP-1-Parte-3/ecommerce_order_payments_dataset.csv',encoding='utf-8')
df4=pd.read_csv('D:/Data Engineer/TP-1-Parte-3/TP-1-Parte-3/ecommerce_orders_dataset.csv',encoding='utf-8')
df5=pd.read_csv('D:/Data Engineer/TP-1-Parte-3/TP-1-Parte-3/ecommerce_products_dataset.csv',encoding='utf-8')

df1.set_index('customer_id', inplace=True)
df2.set_index('order_id', inplace=True)
df3.set_index('order_id', inplace=True)
df4.set_index('order_id', inplace=True)
df5.set_index('product_id', inplace=True)


ctes_unicos = df1['customer_unique_id'].nunique()#devuelve el nro de valores únicos
print(f'\nEl número total de clientes únicos es: {ctes_unicos}')

valor_promedio = df3['payment_value'].mean()#devuelve el promedio
print(f'\nEl valor promedio de pago por pedido es: US$ {round(valor_promedio,2)}')

cat_mas_vendida = df5['product_category_name'].value_counts() #identifica la cantidad de veces que está la categoría
cat_mas_repetida = cat_mas_vendida.idxmax()# identifica el producto que más se repite
cantidad_vendida = cat_mas_vendida.max()#identifica la cantidad de veces
print(f'\nLa categoría más vendida es: "{cat_mas_repetida}", con {cantidad_vendida} unidades vendidas.')

total_pedidos = len(df4)#cuenta la cantidad de filas en el df
print(f'\nEl total de pedidos realizados es de {total_pedidos}.\n')

