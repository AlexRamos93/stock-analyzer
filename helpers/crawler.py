import os
from bs4 import BeautifulSoup, NavigableString, Tag
from urllib.request import urlopen, Request
import yfinance as yf
import requests
from classes.stock import Stock
from helpers.functions import stringToFloat, percentageToNumber, brMonetaryToNumber


def crawBrStocks(ticker):
    elementCounter = 0
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
        "p/b": stringToFloat(values[0]),
        "eps": brMonetaryToNumber(values[1]),
        "ev/ebit": stringToFloat(values[2]),
        "debt/eq": stringToFloat(values[3]),
        "profit margin": percentageToNumber(values[4]),
        "ebit margin": percentageToNumber(values[5]),
        "roic": percentageToNumber(values[6]),
        "payout": percentageToNumber(values[7]),
        "pe/ratio": stringToFloat(values[8]),
        "gross margin": percentageToNumber(values[9]),
        "roe": percentageToNumber(values[10]),
        "roa": percentageToNumber(values[11]),
        "revenue growth": percentageToNumber(values[12]),
        "current ratio": stringToFloat(values[13]),
        "div yield": percentageToNumber(values[14]),
        "beta": values[15],
        "price": values[16]
    }
