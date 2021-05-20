import pandas as pd
import numpy as np
import os
import shutil
import datetime as dt


def readMarketCSV():
    rootPath = '/home/cheeryluck/PycharmProjects/djangoProject2/clean_data/market'
    for root, dirs, files in os.walk(rootPath):
        if 'Stock' not in root:
            for file in files:
                path = os.path.join(root, file)
                if path.endswith('.csv'):
                    filePaths.append(path)
    print('### Load market files completed ###')


def readStockHistoryCSV():
    rootPath = '/home/cheeryluck/PycharmProjects/djangoProject2/clean_data/market/Stock/history'
    for root, dirs, files in os.walk(rootPath):
        for file in files:
            path = os.path.join(root, file)
            if path.endswith('.csv'):
                stockPaths.append(path)
    print('### Load Stock Hisotry files completed ###')


def getNewPath(path):
    return '/home/cheeryluck/PycharmProjects/djangoProject2/analyzed_data' + path[13:]


def getLastDay(path, lastDay):
    df = pd.read_csv(path)
    df.sort_values('Date', inplace=True, ascending=False)
    if df['Date'][0] < lastDay:
        return df['Date'][0]
    return lastDay


def trimLastDay(df, lastDay):
    return df[(df['Date'] <= lastDay)]


def analyzeMarketData(filePath, lastDay):
    df = pd.read_csv(filePath)
    df = trimLastDay(df, lastDay)
 
    df.sort_values('Date', inplace=True, ascending=False)
    df = df.reset_index(drop=True)
    df['LastClose'] = df['Close/Last'].shift(-1)


    if 'DailyRise' in df.columns.values:
        df = df.drop('DailyRise', axis=1)
    if 'Close/Last' in df.columns.values:
        df['DailyRise'] = df['Close/Last'].diff(-1)

  
    if 'DailyRiseRate' in df.columns.values:
        df = df.drop('DailyRiseRate', axis=1)
    if 'DailyRise' in df.columns.values:
        df['DailyRiseRate'] = (df['DailyRise'] / df['LastClose'])


    if 'DailyReturn' in df.columns.values:
        df = df.drop('DailyReturn', axis=1)
    if 'Close/Last' in df.columns.values:
        df['DailyReturn'] = (df['Close/Last'].pct_change(1) + 1).cumprod()


    if 'TotalReturn' in df.columns.values:
        df = df.drop('TotalReturn', axis=1)
    if 'Close/Last' in df.columns.values:
        df['TotalReturn'] = df['Close/Last']
        val = df[df['Date'] == '2020-01-22']['Close/Last']
        df['TotalReturn'] = df['TotalReturn'].apply(lambda x: (x - val) / val)

   
    if 'DailyRiseLog' in df.columns.values:
        df = df.drop('DailyRiseLog', axis=1)
        df['DailyRiseLog'] = (df['Close/Last'].apply(np.log) - df['LastClose'].apply(np.log))

   
    if 'DailyRippleRange' in df.columns.values:
        df = df.drop('DailyRippleRange', axis=1)
    if 'High' in df.columns.values:
        df['DailyRippleRange'] = df['High'] - df['Low']

    
    if 'DailyRippleRadio' in df.columns.values:
        df = df.drop('DailyRippleRadio', axis=1)
    if 'High' in df.columns.values:
        df['DailyRippleRadio'] = df['High'] / df['Low']

    
    if 'DailyK' in df.columns.values:
        df = df.drop('DailyK', axis=1)
    if 'DailyRippleRange' in df.columns.values:
        df['DailyK'] = df['DailyRippleRange'] / df['LastClose']

  
    df.sort_values('Date', inplace=True, ascending=True)
    df = df.reset_index(drop=True)

    
    MA_WindowSize = [5, 15, 30]
    if 'Close/Last' in df.columns.values:
        for i in MA_WindowSize:
            if 'MA' + str(i) in df.columns.values:
                df = df.drop('MA' + str(i), axis=1)
            df['MA' + str(i)] = df['Close/Last'].rolling(i).mean()


    
    EWMA_SPAN = 5
    if 'EWMA' in df.columns.values:
        df = df.drop('EWMA', axis=1)
    if 'Close/Last' in df.columns.values:
        df['EWMA'] = df['Close/Last'].ewm(span=EWMA_SPAN, ignore_na=True, adjust=True).mean()

    
    if 'MACD' in df.columns.values:
        df = df.drop('MACD')
    if 'Close/Last' in df.columns.values:
        MCDA_short = 12
        MCDA_mid = 9
        MCDA_long = 26
        sema = df['Close/Last'].ewm(adjust=False, alpha=2 / (MCDA_short + 1), ignore_na=True).mean()
        lema = df['Close/Last'].ewm(adjust=False, alpha=2 / (MCDA_long + 1), ignore_na=True).mean()
        ema_dif = sema - lema
        dea = ema_dif.ewm(adjust=False, alpha=2 / (MCDA_mid + 1), ignore_na=True).mean()
        df['MACD'] = 2 * (ema_dif - dea)

 
    if 'K' in df.columns.values:
        df = df.drop('K')
    if 'D' in df.columns.values:
        df = df.drop('D')
    if 'J' in df.columns.values:
        df = df.drop('J')
    if 'High' in df.columns.values:
        low_list = df['Low'].rolling(9, min_periods=9).min()
        low_list.fillna(value=df['Low'].expanding().min(), inplace=True)
        high_list = df['High'].rolling(9, min_periods=9).max()
        high_list.fillna(value=df['High'].expanding().max(), inplace=True)
        rsv = (df['Close/Last'] - low_list) / (high_list - low_list) * 100
        df['K'] = pd.DataFrame(rsv).ewm(com=2).mean()
        df['D'] = df['K'].ewm(com=2).mean()
        df['J'] = 3 * df['K'] - 2 * df['D']

 
    
    if 'DailyRise' in df.columns.values:
        RSI_WINDOW = 14
        df['rsi_gain'] = np.select([df['DailyRise'] > 0, df['DailyRise'].isna()], [df['DailyRise'], np.nan], default=0)
        df['rsi_loss'] = np.select([df['DailyRise'] < 0, df['DailyRise'].isna()], [-df['DailyRise'], np.nan], default=0)
        df['avg_gain'] = np.nan
        df['avg_loss'] = np.nan
        df['avg_gain'][RSI_WINDOW] = df['rsi_gain'].rolling(window=RSI_WINDOW).mean().dropna().iloc[0]
        df['avg_loss'][RSI_WINDOW] = df['rsi_loss'].rolling(window=RSI_WINDOW).mean().dropna().iloc[0]
        for i in range(RSI_WINDOW + 1, df.shape[0]):
            df['avg_gain'].iloc[i] = (df['avg_gain'].iloc[i - 1] * (RSI_WINDOW - 1) + df['rsi_gain'].iloc[i]) / RSI_WINDOW
            df['avg_loss'].iloc[i] = (df['avg_loss'].iloc[i - 1] * (RSI_WINDOW - 1) + df['rsi_loss'].iloc[i]) / RSI_WINDOW
      
        df['rs'] = df['avg_gain'] / df['avg_loss']
        df['rsi'] = 100 - (100 / (1 + df['rs']))
        df = df.drop('rsi_gain', axis=1)
        df = df.drop('rsi_loss', axis=1)
        df = df.drop('avg_loss', axis=1)
        df = df.drop('avg_gain', axis=1)

   
    if 'Close/Last' in df.columns.values:
        df['MAD'] = df['Close/Last'].rolling(window=5).apply(lambda x: np.fabs(x - x.mean()).mean())

    df.sort_values('Date', inplace=True, ascending=False)
    df = df.reset_index(drop=True)
    print(getNewPath(filePath))
    df.to_csv(getNewPath(filePath), index=False, header=True)


if os.path.exists('/home/cheeryluck/PycharmProjects/djangoProject2/analyzed_data/'):
    shutil.rmtree('/home/cheeryluck/PycharmProjects/djangoProject2/analyzed_data/', ignore_errors=True)
os.makedirs('/home/cheeryluck/PycharmProjects/djangoProject2/analyzed_data/')
os.makedirs('/home/cheeryluck/PycharmProjects/djangoProject2/analyzed_data/covid-19')
os.makedirs('/home/cheeryluck/PycharmProjects/djangoProject2/analyzed_data/employment')
os.makedirs('/home/cheeryluck/PycharmProjects/djangoProject2/analyzed_data/general')
os.makedirs('/home/cheeryluck/PycharmProjects/djangoProject2/analyzed_data/market/Commodities/Energies')
os.makedirs('/home/cheeryluck/PycharmProjects/djangoProject2/analyzed_data/market/Commodities/Grains')
os.makedirs('/home/cheeryluck/PycharmProjects/djangoProject2/analyzed_data/market/Commodities/Meats')
os.makedirs('/home/cheeryluck/PycharmProjects/djangoProject2/analyzed_data/market/Commodities/Metals')
os.makedirs('/home/cheeryluck/PycharmProjects/djangoProject2/analyzed_data/market/Commodities/Softs')
os.makedirs('/home/cheeryluck/PycharmProjects/djangoProject2/analyzed_data/market/Cryptocurrencies')
os.makedirs('/home/cheeryluck/PycharmProjects/djangoProject2/analyzed_data/market/Currencies')
#os.makedirs('/home/cheeryluck/PycharmProjects/djangoProject2/analyzed_data/market/Funds_ETFs')
os.makedirs('/home/cheeryluck/PycharmProjects/djangoProject2/analyzed_data/market/Index')
os.makedirs('/home/cheeryluck/PycharmProjects/djangoProject2/analyzed_data/market/Stock/history')

filePaths = []
stockPaths = []
readMarketCSV()
lastDay = dt.datetime.now().strftime('%Y-%m-%d')


for filePath in filePaths:
    lastDay = getLastDay(filePath, lastDay)

for filePath in filePaths:
    analyzeMarketData(filePath, lastDay)

COVID_CONFIRMED = '/home/cheeryluck/PycharmProjects/djangoProject2/clean_data/covid-19/time_series_covid19_confirmed_global.csv'
COVID_DEATHS = '/home/cheeryluck/PycharmProjects/djangoProject2/clean_data/covid-19/time_series_covid19_deaths_global.csv'
trimLastDay(pd.read_csv(COVID_CONFIRMED), lastDay).to_csv(getNewPath(COVID_CONFIRMED), index=False, header=True)
trimLastDay(pd.read_csv(COVID_DEATHS), lastDay).to_csv(getNewPath(COVID_DEATHS), index=False, header=True)
