import csv_preprocessing as cp
import subprocess
import dateutility as date
import time

def download_csv():
    cmd = "start chrome \"https://www.nseindia.com/api/corporates-pit?index=equities&from_date="+ date.beforeDate() + "&to_date=" + date.dateToday() + "&csv=true\""
    returned_value = subprocess.call(cmd, shell=True)
    print("Return value for Main Sheet : {}".format(returned_value))
    
def download_stock_csv(stock):
    cmd = "start chrome \"https://www.nseindia.com/api/corporates-pit?index=equities&symbol=" + stock + "&csv=true\""
    returned_value = subprocess.call(cmd, shell=True)
    print("Returned value for {} : {}".format(stock, returned_value))

def getStockCSV():
    fileName = "CF-Insider-Trading-equities-" + date.beforeDate() + "-to-" + date.dateToday() +".csv"
    print(fileName)
    stocks = cp.filterStocks(fileName)
    stockList = stocks.iloc[:, 0].values.tolist()
    #print(stockList)

    for stock in stockList:
        print(stock)
        #download_stock_csv(stock)
        time.sleep(1)


#download_csv()
#time.sleep(20)
getStockCSV()

