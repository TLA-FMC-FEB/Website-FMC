#Import modules
import yfinance as yf
import pandas as pd

#List tickers dalam FMC33Index
tickersList = ['BRPT', 'ANTM', 'INCO', 'SCMA', 'MNCN', 'ERAA', 'CPIN', 'ICBP', 'INDF', 'BYAN', 'ADRO', 'AKRA', 'BBCA', 'BMRI', 'BBRI', 'SIDO', 'KLBF', 'MIKA', 'ASII', 'UNTR', 'ARNA', 'TLKM', 'EXCL', 'TBIG', 'PWON', 'CTRA', 'BSDE', 'EMTK', 'MTDL', 'MLPT', 'TMAS', 'SMDR', 'ASSA']
weight_percentage = []
marketCapList = []
stocks_data = None

def tickersPercentage():
  for i in range(0, len(weight_percentage)):
    try:
      print(f"{tickersList[i]}: {weight_percentage[i]*100:.2f}%")
    except:
      print(tickersList[i] + ": " + str(0))

def toTickersList():
  tickers = []
  for ticker in tickersList:
    tickers.append(ticker + ".JK")
  return tickers

def get_weight_percentage():
  for ticker in toTickersList():
    yf_ticker = yf.Ticker(ticker)
    market_cap = yf_ticker.fast_info['market_cap']
    marketCapList.append(market_cap)
  total_market_cap = sum(marketCapList)
  for market_cap in marketCapList:
    constituent_weight_percentage = market_cap/total_market_cap
    weight_percentage.append(constituent_weight_percentage)
get_weight_percentage()

def get_po():
  all_shares_outstanding = {}

  for ticker_symbol in toTickersList():
    ticker = yf.Ticker(ticker_symbol)
    ticker_info = ticker.info
    
    shares_outstanding = ticker_info.get('sharesOutstanding')
    
    if shares_outstanding is not None:
        all_shares_outstanding[ticker_symbol] = shares_outstanding

def get_fmc33index_data():
  global stocks_data
  stocks_data = yf.download(toTickersList(), start='2025-01-03', end='2025-11-07', progress=False)
  df = pd.DataFrame(stocks_data)
  priceAtTime = df.loc[:, ('Close', toTickersList())]
  weightedPrice = priceAtTime.multiply(weight_percentage, axis=1)
  FMC33Index = weightedPrice.sum(axis=1, skipna=True)
  fmc33_dates = FMC33Index.index.strftime('%Y-%m-%d').tolist()
  fmc33_values = FMC33Index.values.tolist()
  return fmc33_dates, fmc33_values

def get_base_price(date='2025-01-03'):
  if stocks_data is None:
    get_fmc33index_data()
  base_price = stocks_data.loc[date, ('Close', toTickersList())]
  return base_price

def get_fmc33index_info():
  fmc33_largestMarketCap = max(marketCapList)
  fmc33_largestMarketCapIndex = marketCapList.index(fmc33_largestMarketCap)
  fmc33_largestMarketCapCompany = tickersList[fmc33_largestMarketCapIndex]
  fmc33_smallestMarketCap = min(marketCapList)
  fmc33_smallestMarketCapIndex = marketCapList.index(fmc33_smallestMarketCap)
  fmc33_smallestMarketCapCompany = tickersList[fmc33_smallestMarketCapIndex]
  fmc33_meanMarketCap = sum(marketCapList) / len(marketCapList)
  fmc33_medianMarketCap = sorted(marketCapList)[len(marketCapList) // 2]
  fmc33_LargestConstituent = weight_percentage.index(max(weight_percentage))
  fmc33_LargestConstituent = tickersList[fmc33_LargestConstituent]
  fmc33_SmallestConstituent = min(weight_percentage)
  fmc33_SmallestConstituent = weight_percentage.index(fmc33_SmallestConstituent)
  fmc33_SmallestConstituent = tickersList[fmc33_SmallestConstituent]
  fmc33_weightLargestConstituent = max(weight_percentage)
  fmc33_weightTop10Constituent = sum(sorted(weight_percentage, reverse=True)[0:9])
  
  return fmc33_largestMarketCap, fmc33_smallestMarketCap, fmc33_meanMarketCap, fmc33_medianMarketCap, fmc33_LargestConstituent, fmc33_SmallestConstituent, fmc33_weightLargestConstituent, fmc33_weightTop10Constituent

for i in range(0, len(weight_percentage) - 1):
  print(get_base_price().iloc[i])
  