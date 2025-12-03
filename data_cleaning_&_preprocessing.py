import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df=pd.read_csv(url)
print(df)

# to add column
df["finance"]=df["tip"].apply(lambda x:"rich class" if x >=3 else "middle class")
print(df)

#.map() → Element-wise mapping for Series
gender_map = {"Female": "f", "Male": "m"}
df["sex"] = df["sex"].map(gender_map)

#.replace() → Replace specific values
df["day"]=df["day"].replace({"sun": "sunday", "Mon": "Monday"})


df0=df.info()
print(df0)

df1 = df.isnull()
print(df1)

df2=df.isnull().sum()
print(df2)

#in which row have missing value that is group
df4=df.dropna()
print(df4)

#in which column have missing value that is group
df5=df.dropna(axis=1)
print(df5)

#for replace null to mean value
df6=df["tip"].fillna(df['tip'].mean())
print(df6)

# backwardfill and forward fill
#bfill
df7=df.bfill()
print(df7)
#ffill
df8=df.ffill()
print(df8)

# for detect duplicate 
df8=df.duplicated()
print(df8)

df10=df.duplicated('tip','total_bill')
print(df10)

#for delete duplicate
df9=df.drop.duplicates()
print(df9)


#most of the string operation of python is allow in pandas
df11=df["sex"].str.lower()
print(df11)

df12=df["day"].str.contains("sun", case=False)
print(df12)

#Convert column data types:
df["Age"] = df["Age"].astype(int)
df["Date"] = pd.to_datetime(df["Date"])
df["Category"] = df["Category"].astype("category")

