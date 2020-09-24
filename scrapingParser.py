import requests, json
from myparser_HTMLParser import MyHTMLParser
from soupParser import myParser


term = '''"self-sovereign identity"'''
#term = term.replace(" ", "")
sites = ["medium.com"]
search_term = term+"+site:"+sites[0]

params = {'as_epq': search_term, 'num': 100, 'start':0}
api_result = requests.get('https://www.google.com/search', params)
print(api_result.url)
response = api_result.text
print(response)
p = myParser(response)

jsonitems = []
articlesPerPage = -1


while articlesPerPage != 0:
    articlesPerPage = 0
    items = p.getSearchItems()

    for item in items:
        jsonItem = p.dictifyItem(item)
        if jsonItem == None: continue
        jsonitems.append(jsonItem)
        articlesPerPage += 1
        print(jsonItem)

    params['start'] += 100
    print("Starting page ", params['start']/100)
    api_result = requests.get('https://www.google.com/search', params)
    response = api_result.text
    p.updateData(response)
