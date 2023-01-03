import pandas as pd

# Legge il file CSV
df = pd.read_csv("Telefoni_Global.csv", sep=';',encoding='UTF-8',dtype={'rif_cliente': 'object','Utenza 1': 'object','Utenza 2': 'object','Utenza 3': 'object','Utenza 4': 'object','Utenza 5': 'object', 'Utenza 6': 'object','Utenza 7': 'object','Utenza 8': 'object','Utenza 9': 'object'})

# Crea un dizionario per memorizzare i dati per ogni valore di rif_cliente
data = {}

# Per ogni riga del dataframe
for index, row in df.iterrows():
  # Prendi i primi due caratteri di rif_cliente
  key = row["rif_cliente"][:2]
  # Se non c'è ancora una lista per questo valore di rif_cliente, creane una nuova
  if key not in data:
    data[key] = []
  # Aggiungi la riga alla lista
  data[key].append(row)

# Per ogni valore di rif_cliente, crea un nuovo dataframe e salvalo in un file CSV
for key, rows in data.items():
  df = pd.DataFrame(rows)
  df.to_csv(f"{key}_telefoni.csv", index=False, sep=';')
  # print(df)

