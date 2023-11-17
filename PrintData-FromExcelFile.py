import pandas as pd

archivo_excel = "C:\\Users\\Usuario\\Desktop\\file.xlsx"

datos_excel = pd.read_excel(archivo_excel)

print(datos_excel)