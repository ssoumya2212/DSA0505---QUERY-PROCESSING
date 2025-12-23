
import pandas as pd, numpy as np
df=pd.DataFrame({'A':[1,np.nan,3],'B':[4,5,np.nan]})
print(df.fillna(0))
