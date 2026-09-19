#Assignment 5
import pandas as pd

print("="*100)

#1. Create a sample Dataset
df = pd.read_csv("C:/Users/MANTHAN/Desktop/PP Assignments/final_employee_data.csv")
print("=== 1.A Data Set ===")
print(df)

print("="*100)

#2. Filtering (Boolean Indexing)
high_earning_engineers = df[(df['Department'] == 'IT') & (df['Salary'] > 30000)]

print("=== 2.Filtered: High Earning Engineers ===")
print(high_earning_engineers)

print("="*100)

# 3. Sorting
sorted_df=df.sort_values(by=['Join_Year', 'Salary', 'Age'], ascending=[False, False, False])

print("\n=== 3.Sorted: By Rating & Salary (Descending) ===")
print(sorted_df)

print("="*100)

#4. Conditional Selection & Value Assignment
# Method. A: Using df.loc[] to select specific columns based on a condition
top_performers = df.loc[df['Join_Year'] >= 2022, ['Department', 'Salary']]

print("\n=== 4.A.Conditional Selection: Top Performers (Rating >= 4.0)==")
print(top_performers)
print("="*100)

#Method B: Creating a new column conditionally using numpy.where()
import numpy as np 
df['Bonus_Eligible'] = np.where(df['Join_Year'] >= 2022, 'Yes', 'No')

print("\n=== 4.B.Final DataFrame with Conditional 'Bonus_Eligible' Column ===")
print(df)
print("="*100)
df.to_csv("employee_data(Bonus_Eligible).csv", index=False)