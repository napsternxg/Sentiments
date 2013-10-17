"""
Author: Shubhanshu Mishra
Version: 0.1
License: GPL
Credits: Using the mashape api written by Taewook Kang (taewook.kang@gmail.com) from https://www.mashape.com/loudelement/free-natural-language-processing-service
         Please do visit his site http://loudelement.com/ to know more about his exciting projects.
"""

import unirest
from urllib import urlencode

"Class to check for sentiment details in Strings"
class CheckSentiment:
    CHECK_URL=0
    CHECK_STRING=1
    sentiment_analysis_url = "https://loudelement-free-natural-language-processing-service.p.mashape.com/nlp-text/?"

    def __init__(self, choice=None):
        if choice != None:
            self.setAPIURL(choice)

    def setAPIURL(self, choice):
        if choice != self.CHECK_STRING and choice != self.CHECK_URL:
            print "Wrong API Choice. Please try again."
        check_type = "nlp-text" if choice == self.CHECK_STRING else "nlp-url"
        self.key_string = "text" if choice == self.CHECK_STRING else "url"
        self.sentiment_analysis_url = "https://loudelement-free-natural-language-processing-service.p.mashape.com/{0}/?".format(check_type)

    def getEncodedQuery(self, data_string):
        return urlencode({self.key_string:data_string})

    def getResponse(self,data_string):
        request_url = self.sentiment_analysis_url+self.getEncodedQuery(data_string)
        print request_url
        response = unirest.get(request_url, {"X-Mashape-Authorization": "e9AyjmsMW4jb5gMLv9DdMEbncmkLnjpC"})
        return response

    def getSentimentValue(self,data_string):
        response = self.getResponse(data_string)
        return response.body["sentiment-score"]
    
    def getSentiment(self,data_string):
        response = self.getResponse(data_string)
        return response.body["sentiment-text"]

    def showSentimentProcess(self,data_string):
        print "Query String:\n", data_string
        response = self.getResponse(data_string)
        print "Response Headers: ", response.headers
        print "Raw Output:\n", response.raw_body
        print "Sentiment: ", response.body["sentiment-text"]
        print "Sentiment Score: ", response.body["sentiment-score"]
        

    def showSentimentOnInput(self):
        data_string = raw_input("Enter a string/url to analyze it's sentiment: ")
        self.showSentimentProcess(data_string)

if __name__ == "__main__":
    choice = int(raw_input("URL/String[0/1]: "))
    if choice == 1:
        obj = CheckSentiment()
        obj.showSentimentOnInput()
    elif choice == 0:
        obj = CheckSentiment(0)
        obj.showSentimentOnInput()
    else:
        print "Wrong choice"
    
