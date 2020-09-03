import requests
from bs4 import BeautifulSoup as soup
import pprint

response = requests.get("https://bsaber.com/songs/top/?time=all&genre=80s")
page_soup = soup(response.text, "html.parser")
page_tables = page_soup.findAll("div")
print(page_soup.prettify())


