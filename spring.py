import pandas as pd
r = "this is other information about code.It is very important"
time = r.split()
df = pd.DataFrame(time)
print(df)
print(time)
