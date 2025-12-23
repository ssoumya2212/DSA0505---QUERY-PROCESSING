
import pandas as pd, numpy as np
df=pd.DataFrame(np.random.randn(10,4))
df.iloc[2,2]=np.nan
print(df)
