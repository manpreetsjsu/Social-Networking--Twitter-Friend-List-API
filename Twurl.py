import urllib
import oauth2 as oauth


import hidden_github
import json

def augment(url, parameters) :
 secrets = hidden.oauth()
 consumer = oauth.Consumer(secrets['consumer_key'], secrets['consumer_secret'])
 token = oauth.Token(secrets['token_key'],secrets['token_secret'])
 oauth_request = oauth.Request.from_consumer_and_token(consumer,
 token=token, http_method='GET', http_url=url, parameters=parameters)
 oauth_request.sign_request(oauth.SignatureMethod_HMAC_SHA1(), consumer, token)
 return oauth_request.to_url()
