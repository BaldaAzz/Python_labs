import pandas as pd


df = pd.read_csv(r'D:\git\Python_labs\Python_labs\Ruslan\lab_30\titanic.csv')
df.drop("survived pclass sibsp parch embarked who adult_male deck alive alone".split(), axis=1, inplace=True)
#df.head()
print(df)

df_mean = df.groupby(["embark_town", "class", "sex"]).mean()
df_mean['age'] = df_mean['age'].astype(int)
df_mean['fare'] = df_mean['fare'].astype(int)
df_mean
