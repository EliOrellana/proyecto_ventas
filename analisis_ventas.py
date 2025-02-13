import pandas as pd
import numpy as np
import csv


df = pd.read_csv("https://github.com/EliOrellana/proyecto_ventas/blob/ee2f614f418a08338f260a8127c205c8857ac858/ventas_productos.csv")
print (df)

df ['precio_total'] = df['cantidad'] * df['precio'] 
print (df)

plt.bar(df['Producto'], df['precio_total'])
plt.xlabel('Producto')
plt.ylabel('Precio Total')
plt.title('Precio Total por Producto')
plt.savefig('grafico_precios.png')
plt.show()
