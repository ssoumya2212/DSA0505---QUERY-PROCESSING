
import pandas as pd
df=pd.DataFrame({'school_code':['S1','S1','S2'],'age':[12,13,14]})
g=df.groupby('school_code')
print(type(g))
