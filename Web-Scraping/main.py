import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.google.com/search?client=ubuntu&channel=fs&q=ipl+final#sie=m;/g/11vys0dg_g;5;/m/03b_lm1;dt;fp;1;;;")

print(r)