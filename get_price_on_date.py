import yfinance as yf
import pandas as pd

# List of tickers
tickersList = ['BRPT', 'ANTM', 'INCO', 'SCMA', 'MNCN', 'ERAA', 'CPIN', 'ICBP', 'INDF', 'BYAN', 'ADRO', 'AKRA', 'BBCA', 'BMRI', 'BBRI', 'SIDO', 'KLBF', 'MIKA', 'ASII', 'UNTR', 'ARNA', 'TLKM', 'EXCL', 'TBIG', 'PWON', 'CTRA', 'BSDE', 'EMTK', 'MTDL', 'MLPT', 'TMAS', 'SMDR', 'ASSA']

def toTickersList(tickers):
  return [ticker + ".JK" for ticker in tickers]

def get_close_price_for_date(tickers, date):
    start_date = date
    end_date = (pd.to_datetime(date) + pd.DateOffset(days=1)).strftime('%Y-%m-%d')
    data = yf.download(toTickersList(tickers), start=start_date, end=end_date, progress=False)
    return data['Close']

close_prices_on_jan_3 = get_close_price_for_date(tickersList, '2025-01-03')
print("Closing prices on 2025-01-03:")
print(close_prices_on_jan_3)
