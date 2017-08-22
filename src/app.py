import urllib
from bs4 import BeautifulSoup

site = "https://seattle.craigslist.org/search/sss?query=table%20saw&sort=rel"

r = urllib.urlopen(site)
soup = BeautifulSoup(r, "html.parser")
# uls = soup.find_all("ul", class_="rows")
# count=0


class Item:
    def __init__(self, title, img=None, link=None, price=None):
        self.title = title
        self.img = img
        self.link = link
        self.price = price

# for ul in uls:
#     count = count + 1
#     print("{0} entry: {1}".format(count, ul))

print(soup.get_text)
# print(uls[0].li.a.span)
# print(uls[0].li)
# print(uls[0].find("a", class_="result-title").get_text())
# current_item = Item(price=uls[0].li.find("p", class_="result-info"))

# file = open("test", "w")
# file.write(soup.prettify().encode("utf-8"))

