import pandas as pd
df = pd.read_csv("titanic.csv")
df.drop("survived pclass sibsp parch embarked who adult_male deck alive alone".split(), axis=1, inplace=True)
#df.head()
print(df)
