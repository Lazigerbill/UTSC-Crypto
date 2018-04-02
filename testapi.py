# This simple Python script demonstrates
# making a simple rest call to
# XigniteGlobalCurrencies -> ListCurrencies.
# It receives JSON data from the service.
# It parses and displays the data to the console
#

# pip install requests
import requests
import json

# ensure config has the write permissions
from instance.config_file import _token

# Get JSON data to format and print
def printData(jsonText):
    data = json.loads(jsonText)
    print("Open:", data['Open'])


# make a get request to given url


def getUrl(url):
    response = requests.get(url)

    return response


base_url = "http://globalquotes.xignite.com/"
action = "v3/xGlobalQuotes.json/GetGlobalDelayedQuote?IdentifierType=Symbol&Identifier="
ticker = "BAC"
fields = "&_fields=Open,Close,High,Low&_token="

response = getUrl(base_url+action+ticker+fields+_token)
printData(response.text)
