
import pandas as pd
df=pd.DataFrame({'Item':['TV','TV','Mobile'],'Units':[10,20,15]})
print(df.pivot_table(values='Units',index='Item',aggfunc='sum'))
