from datetime import date, timedelta

import pandas as pd
import yfinance as yf
from matplotlib import pyplot as plt

Start = date.today() - timedelta(365)
Start.strftime('%Y-%m-%d')

End = date.today() + timedelta(2)
End.strftime('%Y-%m-%d')

def closing_price(ticker):
    Asset = pd.DataFrame(yf.download(ticker, start=Start,
      end=End)['Adj Close'])     
    return Asset

TESLA = closing_price('TSLA')                  
AMAZON = closing_price('AMZN')

plt.plot(TESLA)
plt.show()

plt.plot(AMAZON)
plt.show()