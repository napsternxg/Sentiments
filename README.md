Sentiments
==========

A python package for the text and URL sentiment analysis method implemented by Taewook Kang (taewook.kang@gmail.com) from https://www.mashape.com/loudelement/free-natural-language-processing-service

Please do visit his site http://loudelement.com/ to know more about his exciting projects.

Usage
-----

`from sentiments import helpers`
Now you can use the helper module from the sentiments package to perform sentiment analysis.
	choice = int(raw_input("URL/String[0/1]: "))
    if choice == 1:
        obj = CheckSentiment()
        obj.showSentimentOnInput()
    elif choice == 0:
        obj = CheckSentiment(0)
        obj.showSentimentOnInput()
    else:
        print "Wrong choice"
		
Credits
-------
Taewook Kang (taewook.kang@gmail.com) from https://www.mashape.com/loudelement/free-natural-language-processing-service