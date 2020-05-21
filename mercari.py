#Mercari App - v0.01
import requests
from lxml import html


#Set user-agent
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
headers = {'User-Agent': user_agent}

#INSERT MERCARI LISTINGS PAGE URL
with open('listings_url.txt', 'r') as url:
    listings_page = url.read()

response = requests.get(listings_page, headers = headers)

assert response.status_code == 200, 'Did not proper access page, time to debug!'

tree = html.fromstring(response.content)

#Collect all listings into a list
listings_list = tree.xpath('/html/body/div/section/section/div/section')

#Generate listing:price pairs
items = {}

#TODO - Include sold tag
for i in range(1,len(listings_list) + 1):
    items[tree.xpath(f'/html/body/div/section/section/div/section[{i}]/a/div/h3/text()')[0]] = tree.xpath(f'/html/body/div/section/section/div/section[{i}]/a/div/div/div/text()')[0]

print("This is your entire listing history (includes sold items)")

#TODO - How can I format this nicely?
for index, item in enumerate(items):
    print(f'{index + 1} - {item}{" "*(50-len(item))}: listed for {items[item]}')