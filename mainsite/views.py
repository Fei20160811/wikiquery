from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    try:
        
        S = requests.Session()
        
        URL = "https://zh.wikipedia.org/w/api.php"
        txtQuery = request.GET['txtQuery']
        
        PARAMS = {
            "action": "parse",
            "page": txtQuery,
            "prop": "text",
            "format": "json"
        }
        
        response = S.get(url=URL, params=PARAMS)
        wikiData = response.json()
        '''wikiFile = open('wikiFile', 'rt')
        wikiData = wikiFile.read()
        wikiFile.close()'''
               
    except:
        wikiData = ""    
    
    return render(request, 'index.html', locals())