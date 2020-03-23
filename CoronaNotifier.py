# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:18:29 2020

@author: amit gupta
"""
""" notification system"""

from plyer import notification
import requests as rq
from bs4 import BeautifulSoup
import time
def notifyMe(title,message):
    notification.notify(
            title=title,
            message=message,
            app_icon="C:\\Users\\amit gupta\\OneDrive\\Desktop\\Assignment\\download.ico",
            timeout=6
        )
    
def getData(url):
    r=rq.get(url)
    return r.text
    
if __name__=="__main__":
    while True:
        notifyMe("Amit","Lets stop the spread of this virus together")
        myHtmlData=getData("https://www.mohfw.gov.in/")
        soup=BeautifulSoup(myHtmlData,'html.parser')
        #print(soup.prettify())
        myDataStr=" "
        for tr in soup.find_all('tbody')[1].find_all('tr'):
              myDataStr +=tr.get_text()
        myDataStr=myDataStr[1:]
        #print(myDataStr.split('\n\n'))
        itemList=myDataStr.split('\n\n')
        states=['Rajasthan','Delhi','Uttar Pradesh']
        for item in itemList[0:22]:
            dataList=item.split('\n')
            if dataList[1]  in states:
                print(dataList)
                nTitle='Cases of COVID-19'
                nText = f"State : {dataList[1]}\nIndian : {dataList[2]} Foriegn : {dataList[3]}\nCoured : {dataList[3]}\nDeaths : {dataList[3]}"
                time.sleep(2)
                notifyMe(nTitle,nText)
            
        time.sleep(6)
        


