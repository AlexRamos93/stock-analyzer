import pandas as pd


def grahamValue(roe, payout, eps, rateYield):
    g = roe * payout
    return eps * (5.5 + (2 * g)) * (4.4 / rateYield)


def getRatioBySector(sector):
    csv = pd.read_csv('./files/pedata.csv')

    for row in csv.iterrows():
        if(row[1][0] == sector):
            return [row[1][2], row[1][8]]


def pegRatio(peRatio, growth):
    return peRatio / (growth * 100)


def stringToFloat(str):
    try:
        return float(str.decode("utf-8").replace(",", "."))
    except:
        return 0.0


def percentageToNumber(str):
    try:
        number = float(str.decode("utf-8").replace("%", "").replace(",", "."))
        return number / 100
    except:
        return 0.0


def brMonetaryToNumber(str):
    try:
        return float(str.decode("utf-8").replace("R$", "").replace(",", "."))
    except:
        return 0.0
