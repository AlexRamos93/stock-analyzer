from helpers.functions import grahamValue, getRatioBySector
# from classes.stock import stock


def valueCalculation(stock, rateYield):
    graham = grahamValue(stock.roe[0], stock.payout, stock.eps, rateYield)
    ratioSector = getRatioBySector(stock.sector)

    return {
        "Graham Value": graham,
        "PEG Ratio": stock.pegRatio,
        "PE Ratio": stock.peRatio,
        "P/B": stock.pb,
        "Sector PE Ratio": ratioSector[0],
        "Sector PEG Ratio": ratioSector[1]
    }
