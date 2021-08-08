#import flair
#sentiment_model_fl = flair.models.TextClassifier.load('en-sentiment')
#title = input("enter a sentence to check its sentiment score: ")
#def sentiment_test(title):
   
    #each_title = flair.data.Sentence(title)
    #sentiment_model_fl.predict(each_title)
    #return(each_title.labels[0].value, each_title.labels[0].score)

#if __name__ == "__main__":
    #title = input("enter a sentence to check its sentiment score: ")
    #z=sentiment_test(title)
    #print(z)


from app.stock_sentiment import sentiment_test
def testing():
    result1=sentiment_test("I am good")
    result2=sentiment_test("I am bad")
    assert result1[0] == "POSITIVE"
    assert result2[0]=="NEGATIVE"
    

