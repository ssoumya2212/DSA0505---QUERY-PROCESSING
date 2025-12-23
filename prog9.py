
import pandas as pd
df=pd.DataFrame({
 'Region':['East','East','West'],
 'Manager':['Martha','Martha','Douglas'],
 'SalesMan':['Alex','Alex','Mike'],
 'Sale_amt':[50000,30000,40000]
})
print(df.pivot_table(values='Sale_amt',index=['Region','Manager','SalesMan'],aggfunc='sum'))
