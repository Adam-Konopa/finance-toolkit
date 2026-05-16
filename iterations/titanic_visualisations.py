# TITANIC DATA VISUAL ANALYSIS

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('data/titanic.csv')

# MATPLOTLIB VISUALIZATIONS
# survival count bar chart
survival_counts = df['Survived'].value_counts()

survival_counts.plot(kind='bar')
plt.title('Survival Counts (0 = No, 1 = Yes)')
plt.xlabel('Survived')
plt.ylabel('Number of Passengers')

plt.show()

# survival rate by gender bar chart
survival_rate_by_gender = df.groupby('Sex')['Survived'].mean()
survival_rate_by_gender.plot(kind='bar')
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate')

plt.show()

# age distribution histogram
plt.hist(df['Age'].dropna(), bins=30, edgecolor='black')
plt.title('Age Distribution of Titanic Passengers')
plt.xlabel('Age')
plt.ylabel('Number of Passengers')

plt.show()

# survival by age (histogram split)
df[df['Survived'] == 1]['Age'].dropna().plot(kind='hist', bins=30, alpha=0.5, label='Survived', edgecolor='black')
df[df['Survived'] == 0]['Age'].dropna().plot(kind='hist', bins=30, alpha=0.4, label='Did Not Survive', edgecolor='black')

plt.title('Age Distribution: Survived vs Did Not Survive')
plt.xlabel('Age')
plt.legend()

plt.show()

# survival by passenger class (bar chart)
survival_rate_by_class = df.groupby('Pclass')['Survived'].mean()
survival_rate_by_class.plot(kind='bar')

plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')

plt.show()

# correlation heatmap
corr = df[['Survived', 'Age', 'Fare', 'Pclass', 'SibSp', 'Parch']].corr()

plt.imshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title('Correlation Heatmap')

plt.show()

# did family size affect survival? (bar chart)
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

survival_rate_by_family_size = df.groupby('FamilySize')['Survived'].mean()
survival_rate_by_family_size.plot(kind='bar')

plt.title('Survival Rate by Family Size')
plt.xlabel('Family Size')
plt.ylabel('Survival Rate')

plt.show() 

# SEABORN VISUALIZATIONS
sns.set_theme(style='whitegrid')

# survival count
sns.countplot(data=df, x='Survived')

plt.title('Survival Counts (0 = No, 1 = Yes)')
plt.show()

# survival by gender
sns.barplot(data=df, x='Sex', y='Survived')

plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate') 
plt.show()

# survival by passenger class
sns.barplot(data=df, x='Pclass', y='Survived')

plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()

# age distribution (kde - smooth probability curve)
sns.histplot(data=df, x='Age', bins=30, kde=True)

plt.title('Age Distribution of Titanic Passengers with KDE')

plt.show()

# survival by age (kde split)
sns.histplot(data=df, x='Age', bins=30, hue='Survived', kde=True, element='step')

plt.title('Age Distribution: Survived vs Did Not Survive (with KDE)')

plt.show()

# box plot of age by survival
sns.boxplot(data=df, x='Survived', y='Age')

plt.title('Age vs Survival (Boxplot)')
plt.xlabel('Survived (0 = No, 1 = Yes)')

plt.show()

# survival by class and gender
sns.barplot(data=df, x='Pclass', y='Survived', hue='Sex')

plt.title('Survival Rate by Passenger Class and Gender')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')

plt.show()

# correlation heatmap with seaborn
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1) 

plt.title('Correlation Heatmap (Seaborn)')

plt.show() 