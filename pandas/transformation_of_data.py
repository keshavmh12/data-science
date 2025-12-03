import pandas as pd
df=pd.read_csv("employee.csv")
print(df)

df1=df.sort_values("age")
print(df1)

df2=df.sort_values("age", ascending=False)
print(df2)

df3=df.sort_values(["age", "salary"]).copy()
print(df3)

df4=df2.reset_index()
print(df4)

df5=df2.reset_index(drop=True)
print(df5)

#df6=df2.reset_index(drop=True, inplacce=True)
#print(df6)

#df7=df.sort_age()
#print(df7)

df8=df2["age"]=df2["salary"].rank()
print(df8)

#Changing Column Order


#df.columns = ["Name", "Age", "City"]

#cols = ["Name"] + [col for col in df.columns if col != "Name"]
#df = df[cols]