import pandas as pd
from finvizfinance.quote import finvizfinance
import flair
import time
import matplotlib.pyplot as plt
from flask import Flask



def lookup_ticker(ticker):
    stock = finvizfinance(ticker)

    news_df = stock.TickerNews()

    #print(news_df)


    # upload the flair model for calculating the sentiments
    sentiment_model_fl = flair.models.TextClassifier.load('en-sentiment')

    df_fl = news_df.copy()

    sentiment_fl = []
    confidence_fl = []



    for news_title in news_df['Title']:
        if news_title.strip() == "":
            sentiment_fl.append("")
            confidence_fl.append("")
        else:
            each_title = flair.data.Sentence(news_title)
            sentiment_model_fl.predict(each_title)
            
            sentiment_fl.append(each_title.labels[0].value)
            confidence_fl.append(each_title.labels[0].score)


    df_fl['sentiment_fl'] = sentiment_fl
    df_fl['confidence_fl'] = confidence_fl

    #df_fl

    df1 = df_fl.replace({"sentiment_fl": {"POSITIVE": 1, "NEGATIVE" : -1}})

    df1['final_confidence_fl'] = df1['sentiment_fl'].astype(int) * df1['confidence_fl']

    #df1
    df1['Date'] = pd.to_datetime(df1['Date']).dt.normalize()
    #df1

    # calculate the median of sentiment score for each day
    median_df_fl1 = df1.groupby(['Date']).median()
    return median_df_fl1



if __name__ == "__main__":




    start_time = time.time()


    # Lets get the news from the API 
    ticker = input('Enter the ticker symbol for the stock: ')
    
    median_df_fl1=lookup_ticker(ticker)

    # the user should see the scores in a printout on the screen
    print(median_df_fl1)

    finish_time = time.time()
    timetaken = finish_time - start_time
    print('Total Run Time for the code was: ', timetaken)


    #create a visualisation for the user to see the trend
    median_df_fl1['final_confidence_fl'].plot()
    plt.show()

    