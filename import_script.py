from urllib.request import urlretrieve
import ssl
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://publicsafety.rpi.edu/campus-security/card-access-schedule'
urlretrieve(url, 'rawdata.html')
soup = BeautifulSoup(open("rawdata.html", encoding="utf8").read(), 'html.parser')

simplelist = []

for row in soup.find_all('tr'):
    temp = ""
    for element in row.find_all('td'):
        temp+=element.next+" "
    if (temp != ""):
        simplelist.append(temp)

print(simplelist)