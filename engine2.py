from soupParser import myParser
import requests, json, sys, time, random

#How this is used:
#1. Initial search is made
#2. next page does the other searches


class Engine:
    def __init__(self):
        self.pageNumber = 1
        self.searchTerm = ""
        self.dictData = []
        self.rawData = ""
        self.params = {'as_epq': self.searchTerm, 'num': 100, 'start':0}
        self.headers = {"user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"}
        self.parser = myParser("")

    def nextPage(self):
        """
        -if initial search not started, throw error
        -if the next page is empty, return false
        -if not, load the next page
        -also initiates search
        """
        if len(self.dictData) == 0:
            raise RuntimeError("Engine has not searched yet")

        self.pageNumber += 1
        self.clear()
        self.params['start'] = (self.pageNumber-1)*100
        success = self.search(self.searchTerm, self.pageNumber)
        if success == False: return False
        else: return True


    def search(self, term, page=1):
        """
        -if search returns nothing, return False
        -return json of results on the page
        {
            "date":12 Dec 2020,
            "title":"Something here",
            ...
        }
        """
        self.clear()
        self.pageNumber = page
        self.params['start'] = (self.pageNumber-1)*100
        self.searchTerm = term
        self.params['as_epq'] = self.searchTerm

        data = self.__search()
        raw = data.text


        
        n = 1
        r = random.randint(1, 1000)
        timeout = (2**n)+(r/1000.0)

        while data.status_code != 200:
            if data.status_code == 429:
                print("Error 429")
                wait = input("Change VPN and press Enter")
                # if "Retry-After" in data.headers.keys():
                #     timeout = data.headers["Retry-After"]
                # print("Error 429. Waiting for ", timeout, "seconds")
                # time.sleep(timeout)

                data = self.__search()
                raw = data.text

                # r = random.randint(1, 1000)
                # n += 1
                # timeout = (2**n)+(r/1000.0)

            else:
                print("Error Code ", data.status_code, ": Quitting...")
                sys.exit()


        self.parser.updateData(raw)

        items = self.parser.getSearchItems()
        for item in items:
            dictItem = self.parser.dictifyItem(item)
            if dictItem == None: continue
            self.dictData.append(dictItem)
            #print(dictItem['date'], dictItem['title'])

        if len(self.dictData) == 0: 
            return False

        else:
            return self.dictData


    def getPageNumber(self):
        return self.pageNumber
    
    def getResults(self):
        return self.dictData

    def clear(self):
        self.rawData = ""
        self.dictData = []

    def resetPageNumber(self):
        self.pageNumber = 1


    def testForResults(self, term):
        tempParams = {'as_epq': term, 'num': 100, 'start':1}
        api_result = requests.get('https://www.google.com/search', tempParams)
        raw = api_result.text
        if "did not match any documents" in raw:
            return False
        else:
            return True


    def __search(self):
        #time.sleep(3)
        api_result = requests.get('https://www.google.com/search', self.params)
        print("URL: ", api_result.url)
        self.rawData = api_result.text
        return api_result
        #f = open("test"+str(self.pageNumber)+".html", "w")
       # f.write(self.rawData)
       # f.close()

        
