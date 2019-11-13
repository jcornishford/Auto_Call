'''
This program makes a call to a phone
'''

from twilio.rest import Client

account_sid = "AC5b51ae547b4da4d350288f00a7269164"
auth_token = "945a131166a7f79acf1a062ae1e8e702"
client = Client(account_sid, auth_token)

call = client.calls.create(	
	url = 'http://demo.twilio.com/docs/voice.xml',
	to = '5107073909',
	from_= '2242314588',
	)

print(call.sid)