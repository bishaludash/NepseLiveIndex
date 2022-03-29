import requests
from datetime import datetime

url="https://www.nepsealpha.com/ajax/live-scan-nepse?fs=10-11-31"
res = requests.get(url)
liveIndex = res.json()
# print(liveIndex)

ltp = liveIndex['ltp']
percentChange = liveIndex['percent_change']
time = liveIndex['time']
startIndex = next(iter( liveIndex['construct'].items() ))
startIndex = startIndex[1]

indexDifferance = float(ltp)-float(startIndex)

print('At: {} ,Current index is {}, percent change: {}%'.format(time, ltp,percentChange ))
print('Star Index : {}, End Index: {}'.format(startIndex, ltp))
print('Change number : ', "{:.2f}".format(indexDifferance) )


def writeLastIndex(ltp, startIndex, date_time_str):
    """
    Store Yesterdays index value for change comparision 
    @ltp : 45, @date_time_str: 2022-03-28 15:00:00
    """
    # check if time is 3PM or greater
    dateTimeObj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    if(dateTimeObj.hour <= 15):
        f = open("lastIndex.csv", "a")
        f.write("{},{},{}\n".format(dateTimeObj.date(),startIndex,ltp))
        f.close()

writeLastIndex(ltp,startIndex,time)