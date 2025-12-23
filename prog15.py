
import pandas as pd, numpy as np
df=pd.DataFrame({'A':[np.nan,np.nan,1],'B':[np.nan,5,np.nan]})
print(df[df.isnull().sum(axis=1)>=2])
