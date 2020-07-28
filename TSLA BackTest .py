import quandl
import pandas as pd
import numpy  as np
import math
import matplotlib.pyplot as plt
import datetime as dt

df = pd.read_csv("C:/Users/Albert Zhang/Desktop/test/TSLA.csv")
df.set_index('Date', inplace=True)

#trading strategy: Buying TSLA when 50 day rolling moving average of TSLA is greater than the intraday volatility

startyear = 2020
startmonth = 1
startday = 1

start=dt.datetime(startyear, startmonth, startday)

now=dt.datetime.now()

vol = 0
volMa50 = 0
wealth = 100000
tsla = 100

for i in df.index:
	close=df['Close'][i]
	vol = df['High'] - df['Low']
	df['vol'] = vol

	volMa50 = df['vol'].rolling(window=50).mean()
	df['volMa50'] = volMa50
	df['result'] = np.where(df['volMa50'] > df['vol'], 'buy signal', 'sell signal')

while tsla > 0:
	if (df['result'] == 'buy signal').all():
		wealth -= close
		tsla += 1
	else:
		wealth += close
		tsla -= 1
	print(wealth)

pctGain = round(100 * (wealth - 100000)/100000)
newWealth = np.around(wealth)


print("")
print("Results from TSLA BackTest:")
print("Starting Wealth: $100,000")
print("Ending Wealth: $" + str(newWealth))
print("Percent Gain: " + str(pctGain) + "%")

print(type(wealth))