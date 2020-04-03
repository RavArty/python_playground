from twilio.rest import Client

account_sid = 'sid'
auth_token = 'auth token'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='from phone number',
    body='test that from python',
    to='phone number'
)

print(message.sid)
