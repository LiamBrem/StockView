import chart

# source of stocks api
import yfinance as yf


def stockInfo(symbol, period, interval):
    # this initializes this shit or sum
    symbol_ticker = yf.Ticker(symbol)

    print("\n" + symbol + period + interval)

    # gets all the information each minute of the entire previous day
    # we should make the period and interval variables
    symbolHistory = symbol_ticker.history(period=period, interval=interval)

    # Each item is just stored in a list within a list
    # this takes the first value of all the Closed values: symbolHistory["Close"][1]
    # could potentially iterate through it
    # if you just do print(symbolHistory) then it will give you everything

    #print(symbolHistory)
    return symbolHistory["Close"][-1]

def retrieveGraph(symbol, period, interval):
    history = yf.Ticker(symbol).history(period=period, interval=interval)

    return chart.getGraphFig(symbol, history)


#stockInfo("AAPL", "1y", "1d")
