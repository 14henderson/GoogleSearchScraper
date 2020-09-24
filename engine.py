from GoogleNews import GoogleNews

class Engine:
    def __init__(self):
        self.news = GoogleNews()
        self.news.setlang('en')
        #self.news.setTimeRange('01/01/2000','01/01/2015')
        self.news.setencode('utf-8')
        self.pageNumber = 1
        self.searchTerm = ""

    def nextPage(self):
        if self.news.result == None:
            raise RuntimeError("Engine has not searched yet")
        self.pageNumber += 1
        self.news.clear()
        self.news.getpage(self.pageNumber)
        if len(self.news.result()) == 0: return False
        else: return True


    def previousPage(self):
        if self.news.result == None:
            raise RuntimeError("Engine has not searched yet")
        self.pageNumber -= 1
        self.news.clear()
        self.news.getpage(self.pageNumber)
        if len(self.news.result()) == 0: return False
        else: return True

    def search(self, term):
        self.news.search(term)
        if len(self.news.result()) == 0:
            return False
        else:
            return self.news.result()

    def getPageNumber(self):
        return self.pageNumber
    
    def getResults(self):
        return self.news.result()

    def clear(self):
        self.news.clear()

    def resetPageNumber(self):
        self.pageNumber = 1
