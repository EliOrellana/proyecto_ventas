import pandas as pd
import numpy as np
import csv

df = pd.read_csv("entorno_ventas\ventas_productos.csv")
print (df)

df ['precio_total'] = df['cantidad'] * df['precio'] 
print (df)

plt.bar(df['Producto'], df['precio_total'])
plt.xlabel('Producto')
plt.ylabel('Precio Total')
plt.title('Precio Total por Producto')
plt.savefig('grafico_precios.png')
plt.show()
