
import pandas as pd, numpy as np
exam_data={'name':['Anastasia','Dima'],'score':[12.5,9]}
labels=['a','b']
df=pd.DataFrame(exam_data,index=labels)
print(df)
