import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result=pd.merge(left=person,right=address,how='left',on='person_id')
    return result[['first_name','last_name','city_name','state_name']]

person={
    'person_id':[1,2],
    'first_name':['travis','billie'],
    'last_name':['sccot','eilish']
}
address={
    'person_id':[1,2],
    'address_id':[1,2],
    'city_name':['pochiniki','bootcamp'],
    'state_name':['erangle','sanhok']
}
person_df=pd.DataFrame(person)
address_df=pd.DataFrame(address)
result_df=combine_two_tables(person_df,address_df)
print(result_df)
