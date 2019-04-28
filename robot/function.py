#coding:utf-8
import requests
import time
now=time.strftime("%m-%d",time.localtime(time.time()))
#历史上的今天
def now_history():
    url="http://api.juheapi.com/japi/toh"
    querystring={"v":1.0,"key":"acaebe9e9d13ef6338c7d0b80e238cd4","month":now.split("-")[0],"day":now.split("-")[1]}
    index=requests.get(url,params=querystring).json()
    for i in index["result"]:
        print(i)



if __name__=="__main__":
    now_history()