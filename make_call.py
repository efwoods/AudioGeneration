# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

account_sid = 'ACa38a0d37c2332b814b5471f988802af2'
auth_token = 'be826f2986df906fbb2075047bbb8da2'
client = Client(account_sid, auth_token)
'''
from twilio.twiml.voice_response import Play, VoiceResponse

response = VoiceResponse()
response.play('https://api.twilio.com/cowbell.mp3', loop=10)

print(response)
'''
call = client.calls.create(
                        #url='http://demo.twilio.com/docs/voice.xml',
                        url='s3://voice-call-audio/output.wav',
                        to='+18439060633',
                        from_='+18432030673'
                    )

print(call.sid)
