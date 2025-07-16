import pandas as pd

datos_candidatos = {
    "nombre": ["Lucia", "Javier", "Elena", "Marcos", "Sofia"],
    "profesion": ["Ingeniero de Datos", "Analista de Negocios", "Cientifico de Datos", "Ingeniero de Datos", "Analista de BI"],
    "experiencia_anios": [6, 4, 8, 3, 5]
}

df_candidatos = pd.DataFrame(datos_candidatos)

ingeniero_datos = df_candidatos[df_candidatos["profesion"] == "Ingeniero de Datos"]
print("los candidatos cuya profesion es ingeniero de datos es:")
print(ingeniero_datos)
candidatos_mas_experiencia = df_candidatos[df_candidatos["experiencia_anios"] >= 5]
print("los candidatos que tienen 5 a;os de experiencia o mas son:")
print(candidatos_mas_experiencia)