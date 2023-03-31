import pandas as pd

df = pd.read_csv("/labs teory python/ЛР30/titanic.csv")

df.drop("survived pclass sibsp parch embarked who adult_male deck alive alone".split(), axis=1, inplace=True)

df_mean = df.groupby(["embark_town", "class", "sex"]).mean()
df_mean['age'] = df_mean['age'].astype(int)
df_mean['fare'] = df_mean['fare'].astype(int)

df = df_mean.reset_index()
df.head()

df_mi = df.set_index(['embark_town', 'class', 'sex'])
df_mi.head()

embark_towns = ['Cherbourg', 'Queenstown', 'Southampton']
classes = ['First', 'Second', 'Third']
sexes =  ['female', 'male']
mi = pd.MultiIndex.from_product([embark_towns, classes, sexes] ,names=['embark_town', 'class', 'sex'])

df_mean.loc[('Queenstown',)]
df_mean.loc[('Southampton', 'Second')]
df_mean.xs('Queenstown')
df_mean.xs(('Southampton', 'First', 'female'))
df_mean.xs('First', level = 'class')
df_mean.loc[('Queenstown', 'Third', 'female'):('Southampton', 'First', 'male')]
df_mean.loc[[('Queenstown', 'Third', 'female'), ('Southampton', 'First', 'male')]]
df_mean.loc[(['Queenstown', 'Southampton'], ['First', 'Second'], ['female', 'male'])]
df_mean.loc[(['Cherbourg', 'Queenstown', 'Southampton'], 'Second', ['female', 'male'])]
df_mean.loc[(slice('Cherbourg', 'Southampton'), 'Second', slice(None))]
df_mean.loc[pd.IndexSlice[:, 'First', :]]
df_mean.reorder_levels(['class', 'sex', 'embark_town']).head()
df_mean.swaplevel(0, 1).head()
df_mean.swaplevel(0, 1).sort_index().head()
df_mean.swaplevel(0, 1).sort_index(level = 'sex').head()

print(mi)
print(df)
