import pandas as pd

df = pd.read_excel("data.xlsx")  # Load data from a CSV file
print(df)

name=df['Name']
print(name)
age=type(df['Age'])
print(age)

numage=df[['Name','Age']]
print(numage)

agecondi=[df['Age']>50]
print(agecondi)

# First row (by label)
row=df.loc[0]
print(row)

# First row (by position)
row2=df.iloc[0]
print(row2)

row3=df.loc[0,'Age']
print(row3)

row4=df.iloc[5,2]
print(row4)

row5=df.loc[0:5,['Age','Name']]
print(row5)

row5=df.iloc[0:5,1:3]
print(row5)

name1=df.at[2,'Name']
print('name1')

name2=df.iat[4,2]
print(name2)

fillter=df[df['Age']>65]
print(fillter)

fillter2=df[(df['Age']>65) & (df['ID']<30)]
print(fillter2)

fillter3=df[(df['Age']>65) | (df['ID']<30)]
print(fillter3)

query1=df.query("Age > 45 and ID<20")
print(query1)

query2=df.query("Age ==45")
print(query2)



