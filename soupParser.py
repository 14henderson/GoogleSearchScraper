from bs4 import BeautifulSoup as bso




class myParser:
    def __init__(self, data):
        self.engine = bso(data, "lxml")

    def getSearchItems(self):
        main = self.engine.find("div", attrs={"id":"main"})
        searchitems = main.findChildren(recursive=False)
        refineditems = []
        for item in searchitems:
            if item.name == "div" and "class" not in item.attrs.keys():
                refineditems.append(item)
        return refineditems
        
    def dictifyItem(self, soupSearchTag):
        titleH3 = soupSearchTag.find("h3", attrs={"class":"zBAuLc"})
        if titleH3 == None: return None
        title = titleH3.find("div").string
        date = soupSearchTag.find("span", attrs={"class":"r0bn4c rQMQod"})
        if date == None: return None
        date = date.string

        return {"title": title, "date":date}


    def updateData(self, data):
        self.engine = bso(data, "lxml")

        

#google.com/search?q=covid&num=100&pws=0&start=100

if __name__ == "__main__":
    our_soup = bso(sample_content, "lxml")
    first_child = our_soup.find()
    print(first_child)