> this is one of the first useful thing i created lol, but i am archiving this since lot of providers are down but if you want the code that do this, check out the [official repo](https://github.com/CYCNO/Direct-Download-API) , here you will find the real code

<div align="center">
<h1 align="center">Direct Download</h1>
<strong><i>A simple yet powerful tool for getting direct download link.</i></strong>
<br>
<br>
<a href="https://www.python.org/">
<img src="https://img.shields.io/badge/MADE%20WITH-PYTHON-red?logoColor=red&logo=Python&style=for-the-badge">
</a>
<a href="https://pypi.org/project/Direct-Download/">
<img src="https://img.shields.io/badge/PYPI-V0.4-blue?logo=PyPI&style=for-the-badge">
</a>
<a href="https://github.com/CYCNO/DirectDownload/graphs/contributors">
<img src="https://img.shields.io/github/contributors/cycno/DirectDownload?style=for-the-badge&color=green&logo=GitHub">
</a>
</div>

---

## Feautres

 - All Information Of File Is Available
 - No Need To Sign Up Or Usage Of Tokens 
 - Data Is In JSON Format 
 - Download the file
 - Switch Between Just Download Link Or ALL Information
 - Very Easy To Use
 
 ## Supported Website

- [AnonFiles](https://anonfiles.com/)
- [Mediafire](https://mediafire.com/)
- [Google Drive](https://drive.google.com/)
- [Myfile](https://myfile.is/)
- [Letsupload](https://letsupload.cc/)
- [Filechan](https://filechan.org/)
- [MegaUpload](https://megaupload.nz/)

## Installation
You Can Install Direct Download Using PIP

```bash
pip install Direct-Download
```

## Quick Start

```py
#First Import Direct From Module
from Direct_Download import Direct

#Declaring Variable As a Class
url = Direct()

#For mediafire
link = url.mediafire('https://www.mediafire.com/view/n2kcs3n9nd88vnr/picture.jpeg/file')
print(link)

#Output
#'https://download1482.mediafire.com/4f1knkpxhq6g/n2kcs3n9nd88vnr/picture.jpeg'

#For Anonfiles
link = url.anonfiles('https://anonfiles.com/n4pdf5Fdy1/night-mountains-minimalist-8k-wo_1_jpeg')
print(link)

#Output
#'https://cdn-126.anonfiles.com/n4pdf5Fdy1/889ab081-1667110179/night-mountains-minimalist-8k-wo (1).jpeg'
```

## Usage/Examples
Get All Information About File `metadata=True`

```py
from Direct_Download import Direct

url = Direct()

#Use Metadata By Enabling Metadata to True
link = url.mediafire('https://www.mediafire.com/file/n2kcs3n9nd88vnr/picture.jpeg/file', metadata=True)
print(link)

# Output
#{'data': {'file': {'metadata': {'DateAndTime': {'date': '2022-10-20',
#                                                'time': '11:00:27'},
#                                'id': 'www.mediafire.com',
#                                'name': 'picture',
#                                'size': {'readable': '73.62KB'}},
#                  'url': {'directDownload': 'https://download1482.mediafire.com/h32ugeuxwitg/n2kcs3n9nd88vnr/picture.jpeg',
#                           'original': 'https://www.mediafire.com/file/n2kcs3n9nd88vnr/picture.jpeg/file'}}},
# 'status': 'true'}
```

Download the file `download=True`
```py
from Direct_Download import Direct

url = Direct()

#Use download By Enabling download to True for downloading your file 
url.mediafire('https://www.mediafire.com/file/n2kcs3n9nd88vnr/picture.jpeg/file', download=True)
```
## Links
- [PyPI](https://pypi.org/project/Direct-Download/)
- [API](https://github.com/CYCNO/Direct-Download-API)

## Contributors
### <a href="https://github.com/CYCNO"><img src="https://avatars.githubusercontent.com/u/90704569?v=4" alt="CYCNO" width="50" height="50" style="border-radius: 50%;"></a>

Contributors are always welcome!
