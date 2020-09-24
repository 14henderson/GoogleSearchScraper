from GoogleNews import GoogleNews
from engine2 import Engine
from data import Catalogue, Interval

engine = Engine()
#terms = ['"self-sovereign identity"', '"self sovereign identity"', 'blockchain identity management']

sites = ["abcnews.go.com", "cnn.com", "nbcnews.com", "huffingtonpost.com", "cbsnews.com", "usatoday.com", "buzzfeed.com", "nytimes.com", "foxnews.com", "dailymail.co.uk", "washingtonpost.com",
"bleacherreport.com", "businessinsider.com", "elitedaily.com", "bbc.co.uk", "cnet.com", "theguardian.com", "msn.com", "npr.org", "nydailynews.com", "latimes.com", "nypost.com", "time.com", "mashable.com",
"sfgate.com", "slate.com", "upworthy.com", "theblaze.com", "telegraph.co.uk", "usnews.com", "vice.com", "chron.com", "gawker.com", "examiner.com", "vox.com", "chicagotribune.com", 
"thedailybeast.com", "salon.com", "mic.com", "mirror.co.uk", "nj.com", "independant.co.uk", "freep.com", "bostonblobe.com", "theatlantic.com", "mlive.com", "engadget.com", "techcrunch.com", 
"boston.com", "al.com", "dallasnews.com"]



term = '''"blockchain"'''
terms = []
for site in sites:
    terms.append(term+" site:"+site)

catalogue = Catalogue(Interval.Month)
results = False


for searchTerm in terms:
    print("Searching for: ", searchTerm)
    engine.clear()

    if engine.testForResults(searchTerm) == False:
        print("No Results Found for ", searchTerm)
        continue
    else:
        results = True

    print("Page 1")
    firstPageResults = engine.search(searchTerm)
    if firstPageResults == False:
        continue
    for article in firstPageResults:
        catalogue.addDate(article)


    while engine.nextPage():
        results = True
        print("Page "+str(engine.getPageNumber()))
        pageResults = engine.getResults()
        for article in pageResults:
            catalogue.addDate(article)

        print(catalogue.getNumEntries(), "entries")
    engine.resetPageNumber()


if results: catalogue.saveData()