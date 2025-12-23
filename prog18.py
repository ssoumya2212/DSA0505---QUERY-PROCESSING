
import pandas as pd
df=pd.DataFrame({'school_code':['S1','S1','S2'],'class':['V','VI','V'],'age':[12,13,14]})
print(df.groupby(['school_code','class']).mean())
