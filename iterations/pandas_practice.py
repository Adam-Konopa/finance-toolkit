# PANDAS PRACTICE USING TITANIC DATASET

import pandas as pd

# Loading titanic dataset
df = pd.read_csv('data/titanic.csv')

# print the first 5 rows 
print(df.head())
print(df.shape)
print(df.columns)

# understanding the data
print(df.info())
print(df.describe())

# viewing selected columns - name and survived status
print(df[['Name', 'Survived']].head())

survivors = df[df['Survived'] == 1]
print(survivors[['Name', 'Survived']].head())

non_survivors = df[df['Survived'] == 0]
print(non_survivors[['Name', 'Survived']].head())

# viewing how many survived 
print(df['Survived'].value_counts())

# viewing how many survived in %
print(df['Survived'].value_counts(normalize=True) * 100)

# viewing how many survived by class (%)
print(df.groupby('Pclass')['Survived'].mean() * 100)

# viewing how many survived by sex (%)
print(df.groupby('Sex')['Survived'].mean() * 100)

# viewing how many survived by gender and class (%)
print(df.groupby(['Sex', 'Pclass'])['Survived'].mean() * 100)

# finding missing data
print(df.isnull().sum())

# finding missing data in the age column
print(df["Age"].isnull().sum())

# filling missing age values with the mean age
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df["Age"].isnull().sum())

# introducing a new column - is a person a child or adult
df['IsChild'] = df['Age'] < 18
print(df[['Name', 'Age', 'IsChild']].head())

# survival rate among children 
print(df.groupby('IsChild')['Survived'].mean() * 100)

# survival rate among children by class, gender
print(df.groupby(['IsChild', 'Pclass', 'Sex'])['Survived'].mean() * 100)

# summary
print('Survival rate overall:')
print(df['Survived'].mean() * 100)

print('\nSurvival rate by gender:')
print(df.groupby ('Sex')['Survived'].mean() * 100)

print('\nSurvival rate by class:')
print(df.groupby('Pclass')['Survived'].mean() * 100)

# 10 oldest passengers
df.sorted_by_age = df.sort_values(by='Age', ascending=False)
print(df.sorted_by_age[['Name', 'Age']].head(10))

# 10 youngest passengers
df.sorted_by_age_a = df.sort_values(by='Age', ascending=True)
print(df.sorted_by_age_a[['Name', 'Age']].head(10))

# 15 pasengers with the highest fare
df.sorted_by_fare = df.sort_values(by='Fare', ascending=False)
print(df.sorted_by_fare[['Name', 'Fare']].head(15))

# rich survivors 
rich_survivors = df[(df['Survived'] == 1) & (df['Fare'] > 100)]
print(rich_survivors[['Name', 'Fare']])

# boys in third class that survived sorted descending by age
boys_third_class_survivors = df[(df['Sex'] == 'male') & (df['Pclass'] == 3) & (df['Survived'] == 1) & (df['Age'] < 18)]
boys_third_class_survivors = boys_third_class_survivors.sort_values(by='Age', ascending=False)
print(boys_third_class_survivors[['Name', 'Age', 'Cabin']].head(20))

# family size 
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = df['FamilySize'] == 1
print(df.groupby("FamilySize")["Survived"].mean() * 100)

# turninng numers into categories
bins = [0, 12, 18, 35, 60, 80]
labels = ['Child', 'Teenager', 'Adult', 'Middle-aged', 'Senior']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)
print(df.groupby('AgeGroup')['Survived'].mean() * 100)

# pivot table for survival rate by sex and class
pivot_table = pd.pivot_table(
    df, 
    values='Survived',
    index='Sex',
    columns='Pclass',   
    aggfunc='mean'
)
print(pivot_table * 100)

# multiple aggregations - mean,max,min, count by class and fare
agg_table = df.groupby('Pclass')['Fare'].agg(['mean', 'max', 'min', 'count'])
print(agg_table)

# correlation between survival, age, fare and passener class
correlation = df[['Survived', 'Age', 'Fare', 'Pclass']].corr()
print(correlation)

# what combnation of factors led to the highest survival rate? 
# columns are sex, class, age group, mean survival rate and count 
df.groupby(["Sex", "Pclass", "AgeGroup"])["Survived"].agg(['mean', 'count'])
print(
    df.groupby(["Sex", "Pclass", "AgeGroup"])["Survived"].agg(['mean', 'count'])
    .sort_values(ascending=False, by='mean')
)