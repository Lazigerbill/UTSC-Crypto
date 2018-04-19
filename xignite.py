# This Python script demonstrates
# making a simple rest call to Xignite API
# It receives JSON data from the service.
# It parses and displays the data
#

import requests
import json
import os

is_prod = os.environ.get('IS_HEROKU', None)
if not is_prod:
    f = open("instance/apikey.txt", 'r')
    _token = f.readline().strip('\n')
else:
    _token = os.environ.get('TOKEN')


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


def getTime():
    base_url = "https://globalquotes.xignite.com/"
    action = "v3/xGlobalQuotes.json/GetGlobalDelayedQuote?IdentifierType=Symbol&Identifier=BAC"
    fields = "&_fields=Message,Time&_token="
    response = requests.get(base_url+action+fields+_token)
    text = response.text
    api_data = json.loads(text)
    return api_data

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
