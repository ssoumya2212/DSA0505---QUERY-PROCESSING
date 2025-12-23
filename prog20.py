
import pandas as pd
df=pd.DataFrame({'name':['Anastasia','James']})
print(df['name'].str.find('an'))
