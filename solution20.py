import pandas as pd
def createBonusColumn(employees):
    employees['bonus']=employees['salary']*2
    return employees
data={'name': ['Alice', 'Bob', 'Charlie'],
        'salary': [3000, 4000, 5000]}
df_employees=pd.DataFrame(data)
result=createBonusColumn(df_employees)
print(result)
    