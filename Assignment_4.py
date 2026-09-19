#Assignment 4
import pandas as pd

df=pd.read_csv("C:/Users/MANTHAN/Desktop/PP Assignments/employee_data.csv")
print(df)

###
print("="*100)
print("1. FINDING NULL VALUES")
print()
missing_data=df.isnull().sum()
print(missing_data)

###
print("="*100)
print("2. FINDING DUPLICATE VALUES")
print()
print("Duplicate values are: ",df.duplicated().sum())

###
print("="*100)
print("3. REMOVING DUPLICATE VALUES")
print()
print(df.drop_duplicates())

###
print("="*100)
print("4. CALCULATING MEAN FOR AGE AND SALARY ")
print()
mean_age = df["Age"].mean()
mean_salary = df["Salary"].mean()
print("Age Mean= ",mean_age)
print("Salary Mean= ",mean_salary)

###
print("="*100)
print("5. FILLING THE NULL VALUES AND DISPLAYING")
print()
df["Age"]=df["Age"].fillna(mean_age)
df["Salary"]=df["Salary"].fillna(mean_salary)
print(df)

###
print("="*100)
print("6. SPLITING THE NAME COLUMN INTO FIRST NAME AND LAST NAME AND ADDING IT TO THE DATAFRAME")
print()
df[["First Name", "Last Name"]] = df["Full Name"].str.split(" ", n=1, expand=True)
print(df)

###
print("="*100)
print("7. REMOVING THE STUDENT FULL NAME COLUMN")
print()
df = df.drop(columns=["Full Name"])
print(df)

###
print("="*100)
print("8. NEW DATAFRAME")
print()
df = df[["Employee_ID","First Name", "Last Name", "Age", "Salary", "Department", "Join_Year"]]
print(df)


df.to_csv("final_employee_data.csv", index=False)