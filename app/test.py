import flair
sentiment_model_fl = flair.models.TextClassifier.load('en-sentiment')
#title = input("enter a sentence to check its sentiment score: ")
def sentiment_test(title):
   
    each_title = flair.data.Sentence(title)
    sentiment_model_fl.predict(each_title)
    return(each_title.labels[0].value, each_title.labels[0].score)

if __name__ == "__main__":
    title = input("enter a sentence to check its sentiment score: ")
    x = sentiment_test(title)

    print(x)