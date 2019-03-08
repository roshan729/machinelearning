import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib notebook
from datetime import datetime
import dateutil.parser

data_url = "https://www.quandl.com/api/v3/datasets/NSE/INFY.csv?"
df1 = pd.read_csv(data_url).sort_values('Date', ascending = False).iloc[:22,:]
data_url = "https://www.quandl.com/api/v3/datasets/NSE/TECHM.csv?"
df2 = pd.read_csv(data_url).sort_values('Date', ascending = False).iloc[:22,:]
df1['Date2'] = df1['Date'].apply(lambda x : dateutil.parser.parse(x))
df2['Date2'] = df2['Date'].apply(lambda x : dateutil.parser.parse(x))

fig, ax = plt.subplots()
a = ax.plot(list(df1["Date2"]), df1["Close"], label="Infosys", alpha=0.5, zorder=10)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Stock Price in 2019")

ax2 = ax.twinx()
b = ax2.plot(list(df2["Date2"]),df2["Close"], alpha=0.5, label="TechM", color="Green")

ax2 = plt.gca()
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

ax2 = plt.gca()
ax2.yaxis.set_visible(False)

# Combine legend
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1+h2, l1+l2, frameon = False)

fig.autofmt_xdate()

plt.show()