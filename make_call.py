'''
This program makes a call to a phone
'''

from twilio.rest import Client

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

call = client.calls.create(	
	url = 'http://demo.twilio.com/docs/voice.xml',
	to = '',
	from_= '',
	)

print(call.sid)
