import requests
import json

def getQuote():
    response = requests.get("https://zenquotes.io/api/random")
    jsonData = json.loads(response.text)
    quote = jsonData[0]['q'] + " - " + jsonData[0]['a']
    return(quote)