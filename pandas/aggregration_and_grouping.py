import pandas as pd
df = pd.DataFrame({
    "Department": ["HR", "HR", "IT", "IT", "Marketing", "Marketing", "Sales", "Sales"],
    "Team": ["A", "A", "B", "B", "C", "C", "D", "D"],
    "Gender": ["M", "F", "M", "F", "M", "F", "M", "F"],
    "Salary": [85, 90, 78, 85, 92, 88, 75, 80],
    "Age": [23, 25, 30, 22, 28, 26, 21, 27],
    "JoinDate": pd.to_datetime([
        "2020-01-10", "2020-02-15", "2021-03-20", "2021-04-10",
        "2020-05-30", "2020-06-25", "2021-07-15", "2021-08-01"
    ])
})  

print(df)

df1=df.groupby("Department")["Salary"].mean()
print(df1)

df2=df.groupby("Team")["Salary"].sum()
print(df2)

df3=df.groupby("Team")["Salary"].count()
print(df3)


df4=df.groupby("Department")["Salary"].min()
print(df4)

df5=df.groupby("Department")["Salary"].max()
print(df5)

df6=df.groupby("Team")["Salary"].agg(["mean","max","min"])
print(df6)

#.transform() Example:
df7=df["Team Avg"] = df.groupby("Team")["Salary"].transform("mean")
print(df7)

#.filter() Example:
df8=df.groupby("Team").filter(lambda x: x["Salary"].mean() > 80)
print(df8)