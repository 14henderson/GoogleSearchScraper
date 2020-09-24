import requests, json, re



class regexGetter():
    def __init__(self):
        pass

    @staticmethod
    def getSingle(test_str, regex):
        matches = re.finditer(regex, test_str, re.MULTILINE)
        numMatches = 0
        toReturn = ""
        for match in matches:
            print("MATCH: ",match)
            numMatches += 1
            #if numMatches > 1:
            #    raise RuntimeError("Incorrect length match. Should be 1, received "+str(numMatches))
            toReturn = match.group()

        if numMatches == 0:
            raise RuntimeError("Incorrect length match. Should be 1, received "+str(numMatches))

        return toReturn


#regex
#REGEX_RESULTS_NUMBER = '''(?<=<div id="result-stats">About ).+(?= results)'''
REGEX_CONTENT = '''(?=<div id="main">).+(?<=<\/div>)'''



#fix search term
term = "self-sovereign identity"
term = term.replace(" ", "+")
sites = ["medium.com"]
search_term = term+"+site:"+sites[0]


params = {'q': search_term}
api_result = requests.get('https://www.google.com/search', params)
#print(api_result.url)
response = api_result.text
f = open("test.html", "w")
f.write(response)
f.close()




# print(response)
#regexGetter.get(response, REGEX_RESULTS_NUMBER)
print(regexGetter.getSingle(response, REGEX_CONTENT))



#data = {"result_count":regexGetter.get(response, REGEX_RESULTS_NUMBER)}
#print(data)
# print the JSON response from Scale SERP
#print(json.dumps(api_result.json()))


