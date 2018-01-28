import datetime
import requests # http://docs.python-requests.org/

# replace with your client information: developer.whereismytransport.com/clients
CLIENT_ID = '266ec63f-cb7c-4048-89c0-3b24d20d1e5d' 
CLIENT_SECRET = 'VZ0SDHRihwycVaiM8GCjKEq2L1lth/zLPJJS3TpR7ns='

payload = {
	"client_id": CLIENT_ID,
	"client_secret": CLIENT_SECRET,
	"grant_type": "client_credentials",
	"scope": "transportapi:all"
}

r = requests.post( 'https://identity.whereismytransport.com/connect/token', data=payload)
if r.status_code != 200:
	raise Exception("Failed to get token")

access_token = r.json()['access_token']

print(access_token)



TOKEN = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjZGMUQ0MDMzNkQ3NjNEREJBNjQwMDkyNTRCNDVGNjcwQTUyMUUxNkYiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJieDFBTTIxMlBkdW1RQWtsUzBYMmNLVWg0VzgifQ.eyJuYmYiOjE1MTcwNTg2ODMsImV4cCI6MTUxNzA2MjI4MywiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS53aGVyZWlzbXl0cmFuc3BvcnQuY29tIiwiYXVkIjoiaHR0cHM6Ly9pZGVudGl0eS53aGVyZWlzbXl0cmFuc3BvcnQuY29tL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IjI2NmVjNjNmLWNiN2MtNDA0OC04OWMwLTNiMjRkMjBkMWU1ZCIsImNsaWVudF9jb3ZlcmFnZSI6Im5NSEFMeG5KbzBHOHNsQ1Q3SkRRaWciLCJjbGllbnRfdGVuYW50IjoiMDk2MGU5NWEtNTVhZi00NTQ0LTlkN2ItNTc2M2NjZWVlYjU0IiwianRpIjoiNTkxZmE0NWI2MWU1Mzc4YTA5OGJkZGRkMDQ5NDc3ODgiLCJzY29wZSI6WyJ0cmFuc3BvcnRhcGk6YWxsIl19.NKfJVffcq_KyCDgyXjQ0PFukyZqEiyXrdFwzCowYauBX91QvZG-cTe-69K4EFoR7-hRoAR3e1KfjrEzYrt9nhkKthPsBkIUoyFukoiTzMJCIGGLQtR3JyR_tUq7APZcUR558kzz814Mg1iJNmG_P3zfJ_svlRG8N4mlEb6uh3gdQA2CAh_62zYDriFbpfIOvNHxNxvtYUF_yK1XmZ1PzHYJKgZ7oXfHLgdpLS6IS02Zo7kGt0rLunPLN3cXvkYt7C6YY_36e-3WFw8GcXDanSPfk0tHMMFnB1GsWQaLMDeKOPI1f-wu8jmcG4tBodtgjrAbeDV597qx6XtO8g0xStQ' 

headers = {
	"Authorization": "Bearer {access_token}".format(access_token=TOKEN),
	"Accept": "application/json"
}

r = requests.get("{ROOT}/agencies".format(ROOT="https://platform.whereismytransport.com/api"), headers=headers)
agencies = r.json()