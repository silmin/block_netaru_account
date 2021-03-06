import json

def searchWord(twitter, word, cnt) :
    url = "https://api.twitter.com/1.1/search/tweets.json"

    params = {'q': word, 'count':cnt, 'result_type':'recent'}
    
    req = twitter.get(url, params = params)

    if req.status_code == 200 :
        searchResults = json.loads(req.text)
        return searchResults['statuses']
    else :
        print("ERROR: %d" % req.status_code)
        return []

