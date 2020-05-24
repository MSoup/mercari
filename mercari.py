#Mercari App - v0.01
import requests
from lxml import html
import csv
import os
import json

#Set user-agent
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
headers = {'User-Agent': user_agent}
my_listings_page = os.environ['LISTING_URL']

response = requests.get(my_listings_page, headers = headers)

if not response.status_code == 200:
    print('Did not proper access page, time to debug!')

tree = html.fromstring(response.content)

#Collect all listings into a list
listings_list = tree.xpath('/html/body/div/section/section/div/section')

listings = []

for index in range(1,len(listings_list) + 1):

    listing = {}
    listing["item"] = tree.xpath(f'/html/body/div/section/section/div/section[{index}]/a/div/h3/text()')[0]
    listing["item_price"] = tree.xpath(f'/html/body/div/section/section/div/section[{index}]/a/div/div/div/text()')[0]
    listing["listing_url"] = tree.xpath(f'/html/body/div/section/section/div/section[{index}]/a/@href')[0]
    listing["sold"] = len(tree.xpath(f"/html/body/div/section/section/div/section[{index}]/a/figure/figcaption//div[contains(@class,'item-sold-out-badge')]")) > 0
    listings.append(listing)

x = json.dumps(listings, sort_keys=True, indent=4, ensure_ascii=False)

with open("test", "w", encoding="utf8") as f:
    f.write(x)


"""
y = json.loads(x)
"""

