import pandas as pd
import numpy as np
import sqlite3

#From Python Lists
data = [
    ["keshav",21,"delhi"],
    ["kunal",22,"noida"],
    ["saket",21,"gurgaon"],
    ["mithha",20,"faridabad"],
    ["agrisha",22,"meerut"],
    ["shreya",21,"ghaziabad"],
    ["vedica",23,"panipat"],
    ["praneeti",22,"ambala"]
]

df = pd.DataFrame(data, columns=['name','age','city'])
print(df)

#From Dictionary of Lists
data_dict={
    "name":["keshav","kunal","saket","mithha","agrisha","shreya","vedica","praneeti"],
     "age":[21,22,21,20,22,21,23,22],
     "city":["delhi","noida","gurgaon","faridabad","meerut","ghaziabad","panipat","ambala"]
}

df2 = pd.DataFrame(data_dict)
print(df2)


#From NumPy Arrays
arr=np.array([[1,2],[3,4]])
df4=pd.DataFrame(arr, columns=['col1','col2'])
print(df4)

#From Excel Files
df5 = pd.read_excel("Mobile_Sales_Data.xlsx")
print(df5)

#From CSV Files
df6 = pd.read_csv("data.csv", usecols=['id','Name','Age','country','email'])
print(df6)                                  

# json data
df7 = pd.read_json("data.json")
print(df7)

#From the Web (Example: CSV from URL)
url="https://www.kaggle.com/datasets/serpilturanyksel/adult-income"
df8 = pd.read_csv(url)
print(df8)

#From SQL Databases
conn = sqlite3.connect("mydb.sqlite")
df = pd.read_sql("SELECT * FROM users", conn)

'''#EDA (Exploratory Data Analysis)
df.head()         # First 5 rows
df.tail()         # Last 5 rows
df.info()         # Column info: types, non-nulls
df.describe()     # Stats for numeric columns
df.columns        # List of column names
df.shape          # (rows, columns)'''