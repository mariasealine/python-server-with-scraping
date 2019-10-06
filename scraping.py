import requests
from bs4 import BeautifulSoup
import re
import json

url = "url to scrape here"

response = requests.get(url)
html_page = response.content
soup = BeautifulSoup(html_page, 'html.parser')

def getSearchResultFromUrl(param):
    fixed_param = param.replace('/', '')
    find_param = soup.body.findAll(text=re.compile(fixed_param))
    response_from_search = json.dumps(find_param)
    return response_from_search
