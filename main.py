import pandas as pd
import json
import datetime as dt
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt

//df = pd.read_json('out.json')

print(f" Number of columns {df.shape[1]}")
print(f" Number of rows {df.shape[0]}")
print(list(df.columns))


with open('out.json') as f:
  d = json.load(f)




plt.show(block=True)

