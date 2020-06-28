import pandas as pd


def grahamValue(roe, payout, eps, rateYield):
    g = roe * payout
    return eps * (5.5 + (2 * g)) * (4.4 / rateYield)


def getRatioBySector(sector):
    csv = pd.read_csv('./files/pedata.csv')

    for row in csv.iterrows():
        if(row[1][0] == sector):
            return {'Current PE': row[1][2], 'PEG Ratio': row[1][8]}