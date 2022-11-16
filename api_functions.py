from datetime import date, timedelta
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#source of stocks api
import yfinance as yf

def stockInfo(symbol):
  symbol = yf.Ticker(symbol)

  return symbol.info

  