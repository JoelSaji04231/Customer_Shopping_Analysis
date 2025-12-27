import pandas as pd
from sqlalchemy import create_engine

df=pd.read_csv("C:/Users/joels/OneDrive/Desktop/Programming/DataAnalystProject/customer_shopping_behavior.csv")

print(df.head())
print(df.info())
print(df.describe(  include='all'))
print(df.isnull().sum()) 

df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum())

df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ', '_')
df=df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})
print(df.columns)

#create column age grp 
labels=["young", "adult","middle_age", "elderly"]
df['age_group']=pd.qcut(df['age'], q=4, labels=labels)
print(df[['age','age_group']].head(10))

#create column purchase_frequency_days
frequency_mapping={
    'Fortnightly': 14,
    'Monthly': 30,
    'Weekly': 7,
    'Daily': 1,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90,
    'Every 6 Months': 180
}
df['purchase_frequency_days']=df['frequency_of_purchases'].map(frequency_mapping)
print(df[['frequency_of_purchases','purchase_frequency_days']].head(10))

print(df[['discount_applied','promo_code_used']].head())
print((df['discount_applied']==df['promo_code_used']).all())

df=df.drop('promo_code_used', axis=1)
print(df.columns)

username='postgres'
password='yourpassword'
host='localhost'
port='5432'
database="customer_behaviour"

engine=create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

table_name='behavior'
df.to_sql(table_name, engine, if_exists='replace', index=False)


print(f"Successfully loaded data into {table_name}")
