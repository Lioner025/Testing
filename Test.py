rom urllib import request
import requests
from bs4 import BeautifulSoup

def search(url):
    main_path = 'https://www.ytdownload.cloud/en6/'
    req = requests.get(main_path)
    soup = BeautifulSoup(req.text,'htmlparser')
    main_link = 'https://www.ytdownload.cloud/en6/conversion/',
    search_url = url


#https://www.ytdownload.cloud/en6/sdownload/k4OO_NA_gUCFVOPWTVkioLK7R0bx9tIX6U6Y7lwUVsQ/
