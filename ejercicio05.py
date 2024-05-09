
import pandas as pd
import requests

data = pd.read_csv ('C://PRACTICA5//clase05-yibenitez//ejercicio clase//frases.csv', header = None) 

for index , row in data.iterrows():
    frase = row [0]
    r = requests.get(f"http://127.0.0.1:5000/prediccion/{frase}")
    prediction = r.json()['prediction']
    print(f"Frase:{frase} - Predicción:{prediction}")

