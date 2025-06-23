import requests
import pandas as pd
import time


# --- STEP 1: List of company symbols (Screener.in codes) ---
company_symbols = [
    "RELIANCE", "TCS", "INFY", "HDFCBANK", "ICICIBANK", "HINDUNILVR", "ITC",
    "KOTAKBANK", "LT", "SBIN", "BHARTIARTL", "BAJFINANCE", "ASIANPAINT",
    "DMART", "WIPRO", "AXISBANK", "MARUTI", "SUNPHARMA", "ULTRACEMCO",
    "TITAN", "ADANIENT", "ADANIPORTS", "COALINDIA", "TECHM", "TATASTEEL",
    "NTPC", "JSWSTEEL", "POWERGRID", "DIVISLAB", "ONGC", "GRASIM", "NESTLEIND",
    "HCLTECH", "BAJAJFINSV", "BRITANNIA", "INDUSINDBK", "BPCL", "EICHERMOT",
    "HAVELLS", "PIDILITIND", "CIPLA", "DRREDDY", "HEROMOTOCO", "M&M",
    "BAJAJ-AUTO", "GAIL", "DABUR", "ICICIPRULI", "SHREECEM", "SIEMENS", "AMBUJACEM", "VEDL", "BANKBARODA", 
    "BIOCON", "SRF", "TRENT", "TVSMOTOR", "CANBK", "TATACONSUM", "TATAPOWER",
    "GODREJCP", "INDIGO", "IOC", "MUTHOOTFIN", "BEL", "TORNTPHARM", "HDFCLIFE", "LUPIN", "PIIND", "NAUKRI", "PETRONET", 
    "INDUSTOWER", "APOLLOHOSP", "VOLTAS", "IDFCFIRSTB", "LICI"
]


dfin = pd.DataFrame()
for ticker in company_symbols:
    df = pd.read_html(f'https://www.screener.in/company/{ticker}/consolidated/#balance-sheet')[6].T
    df.columns = df.iloc[0]
    df = df[1:]
    df.index = df.index.map(lambda x:x[4:])
    df = df['Equity Capital'] + df['Reserves']
    dfin = pd.concat([dfin,df],axis=1)
    print(f"[{company_symbols.index(ticker)+1}/{len(company_symbols)}]: Scraped the Data for {ticker}")
    time.sleep(2) #Polite delay
dfin.columns = company_symbols

dfin.to_excel('net_worth_timeseries.xlsx')

