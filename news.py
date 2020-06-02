from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.divyabhaskar.co.in/coronavirus/')

print(r)
