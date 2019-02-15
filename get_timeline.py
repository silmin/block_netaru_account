import json
from requests_oauthlib import OAuth1Session

def getTimeline(twitter, cnt) :
    timeline_url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params = {'count': cnt}
    res = twitter.get(timeline_url, params = params)

    if res.status_code == 200:
        timelines = json.loads(res.text)
    for line in timelines:
        print(line)
        '''
        print(line['user']['name'])
        print(line['text'])
        print(line['created_at']+'\n')
        '''
    else :
        print("Faild: %d" % res.status_code)

