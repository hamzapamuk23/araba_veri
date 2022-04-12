import requests
from bs4 import BeautifulSoup
data=[]
header ={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
    }

r=requests.get("https://www.arabam.com/ikinci-el/otomobil/bmw",headers=header)
soup=BeautifulSoup(r.content,"html.parser")

modeller=soup.find_all("ul",attrs= {"class":"inner-list"})
for model in modeller:
    modell=model.find_all("li")
    for i in modell:
        link=i.find_all("a",attrs={"class":"list-item"})
        for b in link:
            link_devam=str(b.get("href"))
            link_basi="https://www.arabam.com/"
            seri_link_tamami=link_basi+link_devam
            # print(seri_link_tamami)
           
            detay=requests.get(seri_link_tamami,headers=header)
            detay_soup=BeautifulSoup(detay.content,"html.parser")
            verii=detay_soup.find_all("tr",attrs={"class":"listing-list-item pr should-hover bg-white"})
            for a in verii:
                link=a.find_all("a",attrs={"class":"smallest-text-minus ovh"})
                for bmw in link:
                    link_devam=str(bmw.get("href"))
                    link_basi="https://www.arabam.com/"
                    arabaa_link_tamami=link_basi+link_devam
                    print(arabaa_link_tamami)
                    özellik=requests.get(arabaa_link_tamami,headers=header)
                    özellik_soup=BeautifulSoup(özellik.content,"html.parser")
                                        
                    tek_det=özellik_soup.find_all("div",attrs={"class":"banner-column-detail bcd-mid-extended p10 bg-white"})
                    for i in tek_det:
                        a=i.find_all("li",attrs={"class":"bcd-list-item"})
                        for b in a:
                            et=b.find("span",attrs={"class":"bli-particle bold"}).getText()
                            print(b.getText())
                            # deg=b.find("span",attrs={"class":"bli-particle "})
                            # print(et ,"==", deg)
                    
                    




            





