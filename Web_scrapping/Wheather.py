from bs4 import BeautifulSoup
import requests

URL = "https://www.google.com/search?q=weather&rlz=1C1CHBF_esMX813MX813&oq=wheater&aqs=chrome.1.69i57j0j46j0l5.4339j0j7&sourceid=chrome&ie=UTF-8"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
page = requests.get(URL, headers = headers)
soup = BeautifulSoup(page.content, 'html.parser')
data = {}

data = {'location'    : soup.find(id='wob_loc').get_text(),
        'date'        : soup.find(id='wob_dts').get_text(),
        'description' : soup.find(id='wob_dc').get_text(),
        'humidity'    : soup.find(id='wob_hm').get_text(),
        'rain_prob'   : soup.find(id='wob_pp').get_text(),
        'wind'        : soup.find(id='wob_ws').get_text(),
        'temperature' : soup.find(id="wob_tm").get_text()}

for x, y in data.items():
    print (x + ' -> ' + y)