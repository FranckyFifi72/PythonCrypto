# Create your views here.
import PythonCrypto.TACrypto.Binance as Binance
import PythonCrypto.TACrypto.HistoricalData as HistoricalData
import datetime as dt
import pandas as pd
import PythonCrypto.TACrypto.utilities as ut
import matplotlib.pyplot as plt
import mpld3

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def index ():
  now = dt.datetime.now()
  fromDate = int(dt.datetime.strptime('2022-11-26', '%Y-%m-%d').timestamp() * 1000)
  toDate = int(now.timestamp() * 1000)

  HDBTC = HistoricalData.HistoricalData('BTCUSDT')
  dataBTC = HDBTC.get_historical_data(fromDate, toDate, 2000, '1d')
  dfBTC: pd.DataFrame = ut.get_data_frame(dataBTC)
  htmlBTC = dfBTC.to_html()

  HDETH = HistoricalData.HistoricalData('ETHUSDT')
  dataETH = HDETH.get_historical_data (fromDate, toDate, 2000, '1d')
  dfETH : pd.DataFrame = ut.get_data_frame(dataETH)
  htmlETH = dfETH.to_html()

  print(dfBTC)

  plt.style.use("dark_background")
  # plt.style.use("default")
  width = 0.9  # width of real body
  width2 = 0.05  # width of shadow
  # add a row containing the indices of each row
  dfBTC['indices'] = range(len(dfBTC))

  fig, ax = plt.subplots(figsize=(15, 10))
  # find the rows that are bullish
  dfup = dfBTC[dfBTC.Close >= dfBTC.Open]
  # find the rows that are bearish
  dfdown = dfBTC[dfBTC.Close < dfBTC.Open]
  # plot the bullish candle stick
  ax.bar(dfup['indices'], dfup.Close - dfup.Open, width,
         bottom=dfup.Open, edgecolor='g', color='green')
  ax.bar(dfup['indices'], dfup.High - dfup.Close, width2,
         bottom=dfup.Close, edgecolor='g', color='green')
  ax.bar(dfup['indices'], dfup.Low - dfup.Open, width2,
         bottom=dfup.Open, edgecolor='g', color='green')
  # plot the bearish candle stick
  ax.bar(dfdown['indices'], dfdown.Close - dfdown.Open, width,
         bottom=dfdown.Open, edgecolor='r', color='red')
  ax.bar(dfdown['indices'], dfdown.High - dfdown.Open, width2,
         bottom=dfdown.Open, edgecolor='r', color='red')
  ax.bar(dfdown['indices'], dfdown.Low - dfdown.Close, width2,
         bottom=dfdown.Close, edgecolor='r', color='red')
  ax.grid(color='gray')
  # set the ticks on the x-axis
  ax.set_xticks(dfBTC[::5]['indices'])
  # display the date for each x-tick
  _ = ax.set_xticklabels(labels=
                         dfBTC[::5].index.strftime('%Y-%b-%d'),
                         rotation=45, ha='right')

  html_str = mpld3.fig_to_html(fig)

  template = loader.get_template('Cryptoanalysis/table.html')
  contexte = {'tablehtmlBTC' : htmlBTC, 'tablehtmlETH' : htmlETH, 'graphhtml' : html_str}

  return HttpResponse(template.render(contexte, request))


def display_graph (request):
  names = ['group_a', 'group_b', 'group_c']
  values = [1, 10, 100]

  fig = plt.figure(figsize=(9, 3))

  plt.subplot(131)
  plt.bar(names, values)
  plt.subplot(132)
  plt.scatter(names, values)
  plt.subplot(133)
  plt.plot(names, values)
  plt.suptitle('Categorical Plotting')

  html_str = mpld3.fig_to_html(fig)

  template = loader.get_template('Cryptoanalysis/graph.html')
  contexte = {'graphhtml' : html_str}
   #return render(request, 'Cryptoanalysis/table.html', conexte)
  return HttpResponse(template.render(contexte, request))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    index()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
