from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
hotel_name=[]
hotel_url=[]
hotel_address=[]
hotel_rating=[]
hotel_review_num=[]
hotel_price=[]
hotel_info=[]
check_in=[]
check_out=[]
rooms=[]
hotel_last=[]
url="https://me.cleartrip.com/hotels/united-states/oxford/"
base="https://me.cleartrip.com/"
driver = webdriver.Firefox(executable_path="C:\\Users\\Naresh\\Anaconda3\\Lib\\site-packages\\selenium\\webdriver\\firefox\\geckodriver.exe")
driver.get(url)
soup = BeautifulSoup(driver.page_source)
pages=[]
page =soup.find('div', {"class": "pagination"})
driver.close()
x = page.find_all("a")
for item in x:
    pages.append(item["href"])
pages = list(set(pages))
head =soup.find_all("h2", {"class": "hotels-name"})
links = []
for item in head:
    links.append(item.find("a")["href"])
for link in pages:
    link =base+link[1:]
    driver = webdriver.Firefox(executable_path="C:\\Users\\Naresh\\Anaconda3\\Lib\\site-packages\\selenium\\webdriver\\firefox\\geckodriver.exe")
    driver.get(link)
    soup = BeautifulSoup(driver.page_source)
    head =soup.find_all("h2", {"class": "hotels-name"})
    for item in head:
        links.append(item.find("a")["href"])
    driver.close()
for item in links:
    item = base+item[1:]
    
    driver = webdriver.Firefox(executable_path="C:\\Users\\Naresh\\Anaconda3\\Lib\\site-packages\\selenium\\webdriver\\firefox\\geckodriver.exe")
    driver.get(item)
    soup = BeautifulSoup(driver.page_source)
    try:
        hotel_name.append(soup.find("h1", {"class": "hotel-title"}).text)
    except:
        hotel_name.append("nan")
    try:
        hotel_address.append(soup.find("div", {"class": "hotels-location"}).text)
    except:
        hotel_address.append("nan")
    try:
        hotel_url.append(item)
    except:
        hotel_url.append("nan")
    try:    
        hotel_rating.append(soup.find("span", {"itemprop": "starRating"}).text)
    except:
        hotel_rating.append("nan")
    try:
        amm=soup.find("div", {"itemprop": "aggregateRating"})
        hotel_review_num.append(amm.find("small").text)
    except:
        hotel_review_num.append("nan")
    try:    
        hotel_price.append(soup.find("div", {"class": "hotelMinPriceCont"}).text)
    except:
        hotel_price.append("nan")
    try:   
        li=[]
        amm = soup.find("div",{"id":"Amenities-content"})
        j = amm.find("div",{"class","amenities-description"})
        for p in j.find_all("p"):
            try:
                u = p.b.text
                li.append(p.b.text)
                li.append(p.text)
            except:
                pass
        
        hotel_info.append(li)
    except:
        hotel_info.append(["nan"])
    try:   
        x=[]
        amm = soup.find("div",{"id":"Amenities-content"})
        amm = amm.find("ul",{"class":"list-inline hotel-rules"})
        x = amm.find_all("li")
        m = x[0].text
        m = str(m)
        m.replace("Check-in","")
        check_in.append(m)
        m = x[1].text
        m = str(m)
        m.replace("Check-out","")
        check_out.append(m)
        m = x[2].text
        m = str(m)
        m.replace("rooms","")
        rooms.append(m)
    except:
        rooms.append("nan")
        check_in.append("nan")
        check_out.append("nan")
    try:  
        p=0
        li=[]
        amm = soup.find("div",{"id":"Amenities-content"})
        j = amm.find_all("div",{"class","amenities-category"})
        for i in j:
            if(p==0):
                p = 3
            else:
                io = i.find_all("div")
                for element in io:
                    li.append(element.text)
                    li.append((i.text))
            
                hotel_last.append(li)
    except:
        hotel_last.append("nan")
    try:
        li=[]
        amm = soup.find("div",{"id":"Amenities-content"})
        y = amm.find("div",{"class","amenities-description"})
        try:
            for p in y.find_all("p"):
                li.append(p.b.text)
                li.append(p.text)
        except:
            pass
    except:
        hotel_info.append("nan")
    driver.close()
for item in range(len(check_out)):
    i = check_out[item]
    i= i.split()
    check_out[item]=i[0]

for item in range(len(check_in)):
    i = check_in[item]
    i= i.split()
    check_in[item]=i[0]

for item in range(len(rooms)):
    i = rooms[item]
    i= i.split()
    rooms[item]=i[0]

for item in range(len(hotel_price)):
    i = hotel_price[item]
    i= i.split()
    hotel_price[item]=i[0]

for item in range(len(hotel_rating)):
    i = hotel_rating[item]
    i= i.split()
    hotel_rating[item]=i[0]
for item in range(len(hotel_review_num)):
    i = hotel_review_num[item]
    i= i.split()
    hotel_review_num[item]=i[0]
df = pd.DataFrame(list(zip(rooms, check_in, check_out,hotel_review_num,hotel_rating,hotel_price,hotel_address,hotel_info,hotel_last,hotel_name,hotel_url)),columns=['rooms', 'check_in',' check_out','hotel_review_num','hotel_rating','hotel_price','hotel_address','hotel_info','hotel_last','hotel_name','hotel_url'])
df.to_json("out.json")
