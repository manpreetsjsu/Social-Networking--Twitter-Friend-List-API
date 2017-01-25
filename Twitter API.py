import urllib
import oauth

import json
from Twurl import augment



Twitter_user_status_url= 'https://api.twitter.com/1.1/statuses/user_timeline.json'
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print ''
    acct = raw_input('Enter Twitter Account:')
    if ( len(acct) < 1 ) : break

    url = augment(TWITTER_URL,
    {'screen_name': acct, 'count': '5'} )

    print 'Retrieving', url
    connection = urllib.urlopen(url)

    data = connection.read()
    headers = connection.info().dict

    #print 'Remaining', headers['x-rate-limit-remaining']
    js = json.loads(data)
    print json.dumps(js, indent=4)

    for u in js['users'] :
            print u['screen_name']
            try:
                s = u['status']['text']
                print ' ',s[:70]
            except:
                print('No Status for the USER')

    print 'Remaining Rate Access Limit', headers['x-rate-limit-remaining']


