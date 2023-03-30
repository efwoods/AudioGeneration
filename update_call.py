
import os
from twilio.rest import Client
from twilio.twiml.voice_response import Play, VoiceResponse

account_sid = 'ACa38a0d37c2332b814b5471f988802af2'
auth_token = 'be826f2986df906fbb2075047bbb8da2'

client = Client(account_sid, auth_token)

response = VoiceResponse()


call = client.calls('CAbd58c4f9fd7faac7751b58ab6d6a8b95') \
             .update(twiml=response.play('https://api.twilio.com/cowbell.mp3', loop=10))
print(call.to)