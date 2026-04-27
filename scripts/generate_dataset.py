import pandas as pd
import random
from datetime import datetime, timedelta

clients = ["Ali", "Sara", "Mehdi", "Lea", "Ines", "Omar", "Nora", "Yassine", "Lina", "Hugo", "Amine", "Amina", "Karim", "Sofia"]
regions = ["Paris", "Lyon", "Lille", "Marseille", "Bordeaux", "Toulouse"]
types = ["creation", "formation", "accompagnement", "financement"]

data = []

start_date = datetime(2024, 1, 1)

for i in range(1, 201):  # 200 lignes
    client = random.choice(clients)
    age = random.randint(20, 60)
    region = random.choice(regions)
    type_projet = random.choice(types)
    montant = random.randint(500, 3000)
    date = start_date + timedelta(days=random.randint(0, 365))

    data.append([
        i,
        client,
        age,
        region,
        type_projet,
        montant,
        date.strftime("%Y-%m-%d")
    ])

df = pd.DataFrame(data, columns=[
    "id", "client", "age", "region", "type_projet", "montant", "date"
])

df.to_csv("data/raw/raw_data.csv", index=False)

print("✅ Dataset de 200 lignes généré avec succès !")