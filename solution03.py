import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
data={
"employe_id":[3,90,9,60,49,43], 
"name":["Bob","Alice","Tatiana","Anabelle","Jonathan","Khaled"],
"department":["operations","sales","engineering","information_technology","human_resourses","administration"],
"salary":[48675,11296,33805,37678,23793,40454] 
}
df=pd.DataFrame(data)
print(selectFirstRows(df))
    