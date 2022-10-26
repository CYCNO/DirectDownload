from pprint import pprint
import requests 
from bs4 import BeautifulSoup

class Direct():
    def anonfiles(self,link,metadata=False):
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
            jsondata['directDownload'] = a
            pprint(jsondata)
        elif metadata == False:
            pprint(aDict)  


url = Direct()        
url.anonfiles('https://anonfiles.com/N5C45dE9y5/th_jpeg', metadata=True)