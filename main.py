from helpers.crawler import crawBrStocks
from classes.stock import Stock
from helpers.functions import pegRatio
from helpers.snowflake_analyzer import valueCalculation

stats = crawBrStocks("wege3")
peg = pegRatio(stats['pe/ratio'], stats['revenue growth'])

stock = Stock(stats['name'], 'Machinery', stats['roe'],
              stats['payout'], stats['eps'], stats['pe/ratio'], peg, stats['p/b'])

print(valueCalculation(stock, 2.5))
