import pandas as pd

df = pd.read_csv("creditcard.csv")

# Drop excessive column and duplicates
df.drop_duplicates(inplace=True)
df.drop(["Time", "Amount"], axis=1,inplace=True)

# Export polished dataset
df.to_csv('ETLdata.csv', index=False)