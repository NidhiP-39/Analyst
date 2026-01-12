import pandas as pd
import random
from datetime import datetime, timedelta

data = []
time = datetime.now()

for i in range(100):
    data.append([
        time + timedelta(minutes=i),
        random.randint(20, 40),
        random.randint(100, 300)
    ])

df = pd.DataFrame(data, columns=["Time", "Temperature", "Energy_Usage"])
df.to_csv("dataset.csv", index=False)

print("Dataset generated successfully!")
