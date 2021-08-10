#testing 
from app.stock_sentiment import sentiment_test
def testing():
    result1=sentiment_test("I am good")
    result2=sentiment_test("I am bad")
    assert result1[0] == "POSITIVE"
    assert result2[0]=="NEGATIVE"
    
