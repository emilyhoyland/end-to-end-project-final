# Valence

## About

Valence serves as a tool to decide whether to proceed with a potential investment based on an analysis of positive and negative sentiments for a company’s 100 most recent news headlines. Using FLAIR to generate sentiment scores, Valence will provide a daily median sentiment score to confirm if a company is trending positive or negative and advise whether to invest in a stock on a given day using the following rubric:
 
>-1 to -.51 = Negative Sentiment: Do not invest

>-0.5 to 0.5 = Neutral Sentiment: Further sources should be considered before investing

>0.51 to 1 = Positive Sentiment: Proceed with investment

Simply enter any stock symbol for the company you would like to analyze and let Valence do the work for you!   

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/vivekagarwal14/end-to-end-project-final) under your own control, then "clone" or download your remote copy onto your local computer

We recommend saving it locally as "valence-app".

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd valence-app
```

Use Anaconda to create and activate a new virtual environment, perhaps called "valence-env":

```sh
conda create -n valence-env python=3.8
conda activate valence-env
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above).


## Local Usage

Run the Python script from the root directory:

```py
python app/stock_chart.py
```
```py
# alternative module-style invocation (only required if importing from one file to another):
python -m app.stock_chart
```

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment.

When application has succesfully launched, enter the ticker symbol for you desired stock and hit "Enter."

You may have to wait up to 30 seconds to receive results.

Valence will then generate the daily median sentiment score for the last 100 news headlines using the rubric above. This information will be presented in a line chart, as well as a score in your terminal. You can then use this information to help determine if you want to proceed with your investment today!

>NOTE: To exit the application, close out the line chart window. You will then be able to run the application for your next desired stock!

## Web Application Usage

To use Valence using a web application, make sure you are still in the local repository's root directory.

Run the Python script:

```py
FLASK_APP=web_app flask run
```

When you receive the message: "Running on http://127.0.0.1:5000/", go to your web browser, type in "localhost:5000" and hit "Enter".

Follow instructions on the web application to use Valence's functions.

To exit your session in your terminal, press CTRL+C.


