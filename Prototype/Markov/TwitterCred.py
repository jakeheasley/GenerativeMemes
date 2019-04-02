import json

twitter_cred = dict()

twitter_cred['CONSUMER_KEY'] = 'odz2LjTDt46YAVFjQH7Ys117Z'
twitter_cred['CONSUMER_SECRET'] = 'QCzr4q1z9AiaxvycJlcCg96IqvVtJMgPFmPKsCawVCkvBoP3qU'
twitter_cred['ACCESS_TOKEN'] = '1093246180551786497-uXA24YnqSChYWXc1fDkwHi0nQmif74'
twitter_cred['ACCESS_SECRET'] = 'NYh7nWKduiLRIbqNlINpap10ey1erDlz5rnOO8ZzvRZlv'

with open('twitter_credentials.json', 'w') as secret_creds:
    json.dump(twitter_cred, secret_creds, indent=4, sort_keys=True)
