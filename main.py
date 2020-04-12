from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title,message):
    
    notification.notify(
        title = title,
        message = message,
        app_name = "Covid-19",
        #app_icon = "D:\Python\My Project\COVID-19 Notify in PC\cov.ico",
        timeout = 20
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":


    #notifyMe('snehal','How are You')

    myHtml = getData("https://www.mohfw.gov.in/")
    worldhtml = getData("https://www.worldometers.info/coronavirus/")

    #print(myHtml)

    soup = BeautifulSoup(myHtml, 'html.parser')
    wsoup = BeautifulSoup(worldhtml,'html.parser')

    myStr = []
    world = []
    gj = []
   
    # for all Indian data
    for item in soup.find_all("div",class_="site-stats-count"):
        for strong in item.find_all("strong"):
            myStr.append(strong.get_text())

    # for Gujarat Data     
    for guj in soup.find_all("div",class_="data-table table-responsive"):
        for td in guj.find_all("td"):
            gj.append(td.get_text())
            

    # for World data
    for witem in wsoup.find_all("div",class_="maincounter-number"):
        for span in witem.find_all("span"):
            world.append(span.get_text())
    
    
    print(f"India:-{myStr}")
    print(f"World:-{world}")
    print(f"Gujarat:-{gj[45],gj[46],gj[47],gj[48],gj[49]}")
    
    

    nTitle = "Case Of COVID-19 of Gujarat"
    nText = f"Active Case : {gj[47]}\nCured : {gj[48]}\nDeath : {gj[49]} "
    notifyMe(nTitle,nText)

    time.sleep(2)

    nTitle = "Case Of COVID-19 of INDIA"
    nText = f"Active Case : {myStr[0]}\nCured : {myStr[1]}\nDeath : {myStr[2]}\nMigrate : {myStr[3]} "
    notifyMe(nTitle,nText)

    time.sleep(2)

    nTitle = "Case Of COVID-19 of WORLD"
    nText = f"Active Case : {world[0]}\nCured : {world[1]}\nDeath : {world[2]} "
    notifyMe(nTitle,nText)

    # # print(soup.prettify())
    # for tr in soup.find_all('tbody')[9].find_all('tr'):
    #     myStr += tr.get_text()
    # myStr = myStr[1:]

    # itemList = myStr.split("\n\n")

    # print(itemList)
    # print("total",myStr[0])
    # states = ['Gujarat']

    # for item in itemList[0:]:
    #     dataList = item.split("\n")  
        # print(dataList)
        # if dataList[1] in states:
        #     print("Final list",dataList)
            
            # nTitle = "Case Of COVID-19"
            # nText = f"STATE : {dataList[1]}\nInd : {dataList[2]} & Foreing : {dataList[3]}\nRecover : {dataList[4]}\nDeath : {dataList[5]} "
            # nText = f"STATE : {dataList[1]}\nInd : {dataList[2]}"
            # notifyMe(nTitle,nText)


    
