from pprint import pprint
import requests 
from bs4 import BeautifulSoup
import webbrowser

class Direct():
    def anonfiles(self, link, metadata=False, redirect=False):
        try:
            r = requests.get(link)
            soup = BeautifulSoup(r.content, "html.parser")
            a_href = soup.find("a", {"id": "download-url"}).get("href")
            a = str(a_href)
            aDict = {
                'directDownload' : a
            }
            if metadata == True:
                id = link.split('/', 4)[3]
                jsondata = requests.get(f'https://api.anonfiles.com/v2/file/{id}/info').json()
                jsondata['data']['file']['url']['directDownload'] = a
                return jsondata
            elif redirect:
                webbrowser.open(a)  
            elif redirect and metadata:
                webbrowser.open(a) 
                id = link.split('/', 4)[3]
                jsondata = requests.get(f'https://api.anonfiles.com/v2/file/{id}/info').json()
                jsondata['data']['file']['url']['directDownload'] = a
                return jsondata
            elif metadata == False and redirect==False:
                return aDict 
        except:
            return "Link is Invalid"       

    def mediafire(self, link, metadata=False, redirect=False):
        try:
            down_link = link
            r = requests.get(down_link)
            soup = BeautifulSoup(r.content, "html.parser")
            a_href = soup.find("a", {"class": "input popsok"}).get("href")
            a = str(a_href)
            if metadata:
                id = link.split('/', 4)[2]
                a_byte=soup.find("a", {"class": "input popsok"}).get_text()
                a_name=soup.find("div", {"class": "dl-btn-label"}).get_text()
                details = soup.find("ul", {"class": "details"})
                li_items = details.find_all('li')[1]
                some=li_items.find_all("span")[0].get_text().split()
                dat=list(some)
                down = a_byte.replace(" ","").strip()
                time = dat[1]
                date = dat[0]
                byte = down.split("(",1)[1].split(")",1)[0]
                name = a_name.replace(" ","").strip()
                return {"status": "true","data": {"file": {"url": {'directDownload' : a,"original": link,},"metadata": {"id": id,"name": name,"size": {"readable": byte},"DateAndTime":{"time": time,"date": date}}}}}
            elif redirect:
                webbrowser.open(a)
            elif redirect and metadata:
                webbrowser.open(a)  
                id = link.split('/', 4)[2]
                a_byte=soup.find("a", {"class": "input popsok"}).get_text()
                a_name=soup.find("div", {"class": "dl-btn-label"}).get_text()
                details = soup.find("ul", {"class": "details"})
                li_items = details.find_all('li')[1]
                some=li_items.find_all("span")[0].get_text().split()
                dat=list(some)
                down = a_byte.replace(" ","").strip()
                time = dat[1]
                date = dat[0]
                byte = down.split("(",1)[1].split(")",1)[0]
                name = a_name.replace(" ","").strip()
                return {"status": "true","data": {"file": {"url": {'directDownload' : a,"original": link,},"metadata": {"id": id,"name": name,"size": {"readable": byte},"DateAndTime":{"time": time,"date": date}}}}}
                
            aDict = {'directDownload' : a}
            return aDict
        except:
            return "Link is Invalid"
