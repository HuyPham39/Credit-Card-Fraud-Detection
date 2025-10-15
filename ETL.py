import pandas as pd

df = pd.read_csv("creditcard.csv")

# Drop excessive column and duplicates
df.drop_duplicates(inplace=True)
df.drop(["Time", "Amount"], axis=1,inplace=True)
# For better logit linearity
df.drop(["V17", "V21", "V16", "V27", "V14"], axis=1, inplace=True)

# Export polished dataset
df.to_csv('ETLdata.csv', index=False)