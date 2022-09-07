from get_stock_data import get_most_recent_days, get_data_from_api, get_ticker_symbol
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

data = get_most_recent_days(get_data_from_api(get_ticker_symbol("microsoft")[0]['symbol']), 20)

open = [price["open"] for price in data]

high = [price["high"] for price in data]

low = [price["low"] for price in data]

close = [price["close"] for price in data]

data_4 = np.random.normal(70, 40, 200)


# plot
fig = plt.figure(figsize=(10, 7))

ax = fig.add_axes([0, 0, 1, 1])

# Creating plot
bp = ax.boxplot([[float(low[index]), float(high[index])] for index in range(len(data))])

plt.show()
