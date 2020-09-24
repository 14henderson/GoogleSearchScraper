from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = False
        self.data = []

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            #print(attrs)
            if ('id', 'main') in attrs:
                self.recording = True

    def handle_endtag(self, tag):
        if tag == "div" and self.recording:
            self.recording = False
            print(self.data)
        #print(tag)
        #if tag == "div" and "id" in attrs and "main" in attrs:
            #print("In main tag!")

    def handle_data(self, data):
        if self.recording:
            self.data.append(data)

if __name__ == "__main__":
    p = MyHTMLParser()