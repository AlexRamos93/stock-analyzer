import matplotlib.pyplot as plt
import os
from bs4 import BeautifulSoup, NavigableString, Tag
from urllib.request import urlopen, Request
import yfinance as yf
import numpy as np
from pandas_datareader import DataReader
from yahoo_fin import stock_info as si
import pandas as pd
import requests
