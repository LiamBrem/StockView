from datetime import date, timedelta
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#source of stocks api
import yfinance as yf

def stockInfo(symbol):
  #this initializes this shit or sum
  symbol = yf.Ticker(symbol)

  #gets all the information each minute of the entire previous day
  #we should make the period and interval variables
  symbolHistory = symbol.history(period="1d",interval="1m")

  #Each item is just stored in a list within a list
  #this takes the first value of all the Closed values
  #could potentially iterate through it
  #if you just do print(symbolHistory) then it will give you everything
  print(symbolHistory)

  print(symbolHistory["Close"][1])
  

  #bruh 
  return symbolHistory["Close"][-1]

  
stockInfo("AEO")