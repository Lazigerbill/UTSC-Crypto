# This simple Python script demonstrates
# making a simple rest call to
# XigniteGlobalCurrencies -> ListCurrencies.
# It receives JSON data from the service.
# It parses and displays the data to the console
#

# pip install requests
import requests
import json
import os

is_prod = os.environ.get('IS_HEROKU', None)
if not is_prod:
    f = open("instance/apikey.txt", 'r')
    _token = f.readline().strip('\n')
# def settoken():
#     _token = os.environ['TOKEN']
#     return
# Get JSON data to format and print

def printData(jsonText):
    data = json.loads(jsonText)
    return data


# make a get request to given url


def getUrl(ticker):
    base_url = "http://globalquotes.xignite.com/"
    action = "v3/xGlobalQuotes.json/GetGlobalDelayedQuote?IdentifierType=Symbol&Identifier="
    fields = "&_fields=Last,PercentChangeFromPreviousClose,Volume,Time&_token="
    response = requests.get(base_url+action+ticker+fields+_token)
    text = response.text
    api_data = json.loads(text)

    return api_data


response1 = getUrl("HK")
# create dictionaries for all fields

def lastDict():
    d = {}
    return d


def volumeDict():
    d = {}
    return d


def percentchangeDict():
    d = {}
    return d
