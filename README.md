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
<img src="https://img.shields.io/github/contributors/cycno/justudy?style=for-the-badge&color=green&logo=GitHub">
</a>
</div>

---

## Feautres

 - All Information Of File Is Available
 - No Need To Sign Up Or Usage Of Tokens 
 - Data Is In JSON Format 
 - Redirect link in default browser
 - Switch Between Just Download Link Or ALL Information
 - Very Easy To Use
 
 ## Supported Website

- [AnonFiles](https://anonfiles.com/)
- [Mediafire](https://mediafire.com/)
- More Added Soon...

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
#{'directDownload': 'https://download1482.mediafire.com/4f1knkpxhq6g/n2kcs3n9nd88vnr/picture.jpeg'}

#For Anonfiles
link = url.anonfiles('https://anonfiles.com/n4pdf5Fdy1/night-mountains-minimalist-8k-wo_1_jpeg')
print(link)

#Output
#{'directDownload': 'https://cdn-126.anonfiles.com/n4pdf5Fdy1/889ab081-1667110179/night-mountains-minimalist-8k-wo (1).jpeg'}
```

## Usage/Examples
Get All Information About File `metadata=True`

```py
from Direct_Download import Direct
from pprint import pprint

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

Open Link In Your Browser `redirect=True`
```py
from Direct_Download import Direct

url = Direct()

#Use Redirect By Enabling Redirect to True
url.mediafire('https://www.mediafire.com/file/n2kcs3n9nd88vnr/picture.jpeg/file', redirect=True)
```
## Links
- [PyPI](https://pypi.org/project/Direct-Download/)

## Contributors
- [@CYCNO](https://github.com/CYCNO)

Contributors are always welcome!
