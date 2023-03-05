import requests
from yahoo_fin import stock_info as si
from dataclasses import dataclass;

url = "https://twelve-data1.p.rapidapi.com/stocks"

querystring = {"exchange":"NASDAQ","format":"json"}

headers = {
	"X-RapidAPI-Key": "aa32ba9197msh1365ae1cd294779p16c5ccjsn10d314297054",
	"X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)


@dataclass
class Stock:
    companyName: str
    price: int
    pe_ratio: float
    eps: int
    dividend: int
    score = 50

company50List = (
'AAPL',
'MSFT',
'AMZN',
'GOOGL',
'BRK.B',
'GOOG',
'NVDA',
'XOM',
'UNH',
'JNJ',
'JPM',
'TSLA',
'V',
'PG',
'MA',
'HD',
'CVX',
'META',
'LLY',
'MRK',
'ABBV',
'PFE',
'BAC',
'AVGO',
'KO',
'PEP',
'TMO',
'COST',
'WMT',
'MCD',
'DIS',
'CSCO',
'ABT',
'CMCSA,'
'WFC',
'DHR',
'ACN',
'VZ',
'ADBE',
'NFLX',
'LIN',
'PM',
'NKE',
'TXN',
'CRM',
'BMY',
'NEE',
'COP',
'RTX',
'QCOM')
top10List = [10]
avoidList = [10]

#get company name (inputed by user thorugh UI)
companyName = company50List[2]

#create quote table for a given stock
quote_table = si.get_quote_table(companyName)

#get stock price
price = quote_table["Quote Price"]

#get stock price to earnings ratio
PERatio = quote_table["PE Ratio (TTM)"]

#get stock earnings per share
earnings_per_share = quote_table["EPS (TTM)"]

#get stock stock dividend
dividendstr = quote_table["Forward Dividend & Yield"]
spc = dividendstr.find(" ")
dividend = dividendstr[:spc]
if dividend == 'N/A':
    dividend = 0
div_yield = float(dividend) / price

#create new stock (using pre determined variables)
stockTest = Stock(companyName, price, PERatio, earnings_per_share, dividend)

#test for values
print("Company: " + stockTest.companyName)
print("Stock price: " + str(stockTest.price))
print("PE Ratio: " + str(stockTest.pe_ratio))
print(dividend)
print(earnings_per_share)
print(div_yield)
