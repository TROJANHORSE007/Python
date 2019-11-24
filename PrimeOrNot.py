from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
my_url= 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'

uClient=uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")


containers = page_soup.findAll("div",{"class": "bhgxx2 col-12-12"})
#print(len(containers))

containers = page_soup.findAll("div",{"class": "bhgxx2 col-12-12"})
print(len(containers))

print(soup.prettify(containers[0]))