import pandas as pd
#Pandas is built on two main data structures:

#Series → One-dimensional (like a single column in Excel)
#DataFrame → Two-dimensional (like a full spreadsheet or SQL table)

# 1D labeled array
s = pd.Series([10,20,30,40,50,60])
print(s)

# 2D labeled data structure
data={
    "name":["keshav","kunal","saket","mithha","agrisha","shreya","vedica","praneeti"],
     "age":[21,22,21,20,22,21,23,22],
     "city":["delhi","noida","gurgaon","faridabad","meerut","ghaziabad","panipat","ambala"]
}

df = pd.DataFrame(data)
print(df)

di= df.index
print(di)

dc = df.columns
print(dc)