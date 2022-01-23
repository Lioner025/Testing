from urllib import request
import requests
from bs4 import BeautifulSoup

def search(url):
    conversion = 'https://www.ytdownload.cloud/en6/conversion/'
    formdata = {'url':url}
    req = requests.post(conversion,data=formdata)
    soup = BeautifulSoup(req.text,'htmlparser')
    format = soup.find_all('a',{'class':'dlbnt'})
