import requests 
import json
import wget

BASE_URI = 'https://ddl-api.cycno.repl.co/'


class Direct():
    def mediafire(self, link, metadata=False, download=False):
        down = requests.get(f'{BASE_URI}mediafire?link={link}').json()
        down_link = down['data']['file']['url']['directDownload']
        
        if metadata and download:
            ok = wget.download(down_link)
            print(f' download completed as {ok}')  
            return json.dumps(down)  
        if metadata:
            return json.dumps(down)
        if download:
            return f' filename: {wget.download(down_link)}'
        return down_link

    def google_drive(self, link, metadata=False, download=False):
        down = requests.get(f'{BASE_URI}gdrive?link={link}').json()
        down_link = down['data']['file']['url']['directDownload']
        
        if metadata and download:
            ok = wget.download(down_link)
            print(f' download completed as {ok}')  
            return json.dumps(down)  
        if metadata:
            return json.dumps(down)
        if download:
            return f' filename: {wget.download(down_link)}'
        return down_link

    def anonfiles(self, link, metadata=False, download=False):
        down = requests.get(f'{BASE_URI}anonfiles?link={link}').json()
        down_link = down['data']['file']['url']['directDownload']
        
        if metadata and download:
            ok = wget.download(down_link)
            print(f' download completed as {ok}')  
            return json.dumps(down)  
        if metadata:
            return json.dumps(down)
        if download:
            return f' filename: {wget.download(down_link)}'
        return down_link
    
    def letsupload(self, link, metadata=False, download=False):
        down = requests.get(f'{BASE_URI}letsupload?link={link}').json()
        down_link = down['data']['file']['url']['directDownload']
        
        if metadata and download:
            ok = wget.download(down_link)
            print(f' download completed as {ok}')  
            return json.dumps(down)  
        if metadata:
            return json.dumps(down)
        if download:
            return f' filename: {wget.download(down_link)}'
        return down_link
    
    def filechan(self, link, metadata=False, download=False):
        down = requests.get(f'{BASE_URI}filechan?link={link}').json()
        down_link = down['data']['file']['url']['directDownload']
        
        if metadata and download:
            ok = wget.download(down_link)
            print(f' download completed as {ok}')  
            return json.dumps(down)  
        if metadata:
            return json.dumps(down)
        if download:
            return f' filename: {wget.download(down_link)}'
        return down_link
    
    def megaupload(self, link, metadata=False, download=False):
        down = requests.get(f'{BASE_URI}megaupload?link={link}').json()
        down_link = down['data']['file']['url']['directDownload']
        
        if metadata and download:
            ok = wget.download(down_link)
            print(f' download completed as {ok}')  
            return json.dumps(down)  
        if metadata:
            return json.dumps(down)
        if download:
            return f' filename: {wget.download(down_link)}'
        return down_link
    
    def myfile(self, link, metadata=False, download=False):
        down = requests.get(f'{BASE_URI}myfile?link={link}').json()
        down_link = down['data']['file']['url']['directDownload']
        
        if metadata and download:
            ok = wget.download(down_link)
            print(f' download completed as {ok}')  
            return json.dumps(down)  
        if metadata:
            return json.dumps(down)
        if download:
            return f' filename: {wget.download(down_link)}'
        return down_link
