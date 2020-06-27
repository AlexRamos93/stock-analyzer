import matplotlib.pyplot as plt
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import yfinance as yf
import numpy as np
from pandas_datareader import DataReader
from yahoo_fin import stock_info as si
import pandas as pd
import requests


status_url = 'https://www.sunoresearch.com.br/acoes/'

# tables = {}

tickers = ['JHSF3', "WEGE3", "ITUB3", "TRIS3", "WIZS3", "TOTS3"]

parsed_values = []

for ticker in tickers:
    elementCounter = 0
    fundamentals = [ticker]
    url = status_url + ticker
    req = Request(url=url)
    response = urlopen(req)
    html = BeautifulSoup(response, "lxml", from_encoding="UTF-8")
    tables = html.find(id="indicators-table")
    # tables[ticker] = table

    # for file_name, table in tables.items():
    for x in tables.findAll('td'):
        elementCounter += 1
        if (elementCounter == 2):
            fundamentals.append(x.renderContents())
        elif (elementCounter == 12):
            fundamentals.append(x.renderContents())
        elif (elementCounter == 14):
            fundamentals.append(x.renderContents())
        elif (elementCounter == 16):
            fundamentals.append(x.renderContents())
        elif (elementCounter == 18):
            fundamentals.append(x.renderContents())
        elif (elementCounter == 20):
            fundamentals.append(x.renderContents())
        elif (elementCounter == 26):
            fundamentals.append(x.renderContents())
        elif (elementCounter == 26):
            fundamentals.append(x.renderContents())
        elif (elementCounter == 34):
            fundamentals.append(x.renderContents())
        elif (elementCounter == 48):
            fundamentals.append(x.renderContents())
        elif (elementCounter == 50):
            fundamentals.append(x.renderContents())
        elif (elementCounter == 52):
            fundamentals.append(x.renderContents())
        elif (elementCounter == 54):
            fundamentals.append(x.renderContents())
        elif (elementCounter == 56):
            fundamentals.append(x.renderContents())
        elif (elementCounter == 58):
            fundamentals.append(x.renderContents())

    stock = yf.Ticker(ticker + ".SA")
    try:
        fundamentals.append(stock.info["beta"])
    except:
        fundamentals.append("")

    parsed_values.append(fundamentals)


columns = ["TICKER", 'P/VP', 'EV/EBIT', 'DIV. LIQUIDA/PL', 'Marg. Liquida',
           'Marg. EBIT', 'ROIC', 'Payout', 'P/L', 'Marg. Bruta', 'ROE', 'ROA', 'Crec. Rec (5a)', 'Liquidez Corrente', 'Div. Yield', "Beta"]

df = pd.DataFrame(parsed_values, columns=columns)

df.to_csv('stocks.csv')
