import os
from bs4 import BeautifulSoup, NavigableString, Tag
from urllib.request import urlopen, Request
import yfinance as yf
import requests
from classes.stock import Stock


def crawBrStocks(ticker):
    values = []
    url = 'https://www.sunoresearch.com.br/acoes/' + ticker
    req = Request(url=url)
    response = urlopen(req)
    html = BeautifulSoup(response, "lxml", from_encoding="UTF-8")
    tables = html.find(id="indicators-table")

    for x in tables.findAll('td'):
        elementCounter += 1
        if (elementCounter == 2):
            values.append(x.renderContents())
        elif (elementCounter == 10):
            values.append(x.renderContents())
        elif (elementCounter == 12):
            values.append(x.renderContents())
        elif (elementCounter == 14):
            values.append(x.renderContents())
        elif (elementCounter == 16):
            values.append(x.renderContents())
        elif (elementCounter == 18):
            values.append(x.renderContents())
        elif (elementCounter == 20):
            values.append(x.renderContents())
        elif (elementCounter == 26):
            values.append(x.renderContents())
        elif (elementCounter == 34):
            values.append(x.renderContents())
        elif (elementCounter == 48):
            values.append(x.renderContents())
        elif (elementCounter == 50):
            values.append(x.renderContents())
        elif (elementCounter == 52):
            values.append(x.renderContents())
        elif (elementCounter == 54):
            values.append(x.renderContents())
        elif (elementCounter == 56):
            values.append(x.renderContents())
        elif (elementCounter == 58):
            values.append(x.renderContents())

    stock = yf.Ticker(ticker + ".SA")
    try:
        values.append(stock.info["beta"])
        values.append(stock.info["previousClose"])
    except:
        values.append("")

    return {
        "p/b": values[0],
        "eps": values[1],
        "ev/ebit": values[2],
        "debt/eq": values[3],
        "profit margin": values[4],
        "ebit margin": values[5],
        "roic": values[6],
        "payout": values[7],
        "pe/ratio": values[8],
        "gross margin": values[9],
        "roe": values[10],
        "roa": values[11],
        "revenue growth": values[12],
        "current ratio": values[13],
        "div yield": values[14],
        "beta": values[15],
        "price": values[16]
    }
