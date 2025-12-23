
import pandas as pd
df=pd.DataFrame({'Item':['TV','TV','Mobile'],'Sale_amt':[50000,70000,30000]})
print(df.pivot_table(values='Sale_amt',index='Item',aggfunc=['min','max']))
