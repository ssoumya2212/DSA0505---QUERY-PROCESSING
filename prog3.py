
import pandas as pd
df = pd.DataFrame({'JOB_TITLE':['President','Manager','Clerk','Programmer']})
print(df.sort_values(by='JOB_TITLE', ascending=False))
