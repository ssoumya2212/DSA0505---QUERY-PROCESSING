
import pandas as pd
df = pd.DataFrame({'EMPLOYEE_ID':[101,101,102,176,176,200,200]})
print(df['EMPLOYEE_ID'].value_counts()[lambda x: x>=2].index.tolist())
