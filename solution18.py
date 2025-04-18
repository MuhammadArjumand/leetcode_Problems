import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], ignore_index=True)
df1 = pd.DataFrame({
    'student_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [20, 21, 22]
})

df2 = pd.DataFrame({
    'student_id': [4, 5, 6],
    'name': ['David', 'Eve', 'Frank'],
    'age': [23, 24, 25]
})

result = concatenateTables(df1, df2)
print(result)
