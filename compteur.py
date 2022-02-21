from googleapiclient.discovery import build
import requests
import json

api_key ='CLE_API'

youtube = build ('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
		part='statistics',
		id='ID_CHAINE'
	)

response: object = request.execute()

print(response)

abo = response['items'][0]['statistics']['subscriberCount']

print (abo)

aboint = float(abo)

abok = float(aboint/1000)

print (abok)


abodisplay = str(abok)+"K"

print (abodisplay)
