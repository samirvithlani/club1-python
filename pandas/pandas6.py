import pandas as pd
import numpy as np

np.random.seed(0)
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))
df = df.add(100)

print(df)