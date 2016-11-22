import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1
alchemy_language = AlchemyLanguageV1(api_key='4b25c177505967add72f5193efd43e4aeb272bb4')


#request.json['comment']

sentiment=json.loads(json.dumps(alchemy_language.sentiment("Great", language='english'), indent=2))['docSentiment']['score']

print sentiment
print type(sentiment)
