# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
def TextMessage(plaintext):
    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "ACebd064fa9348992fc4e79ca4640381e2"
    auth_token  = "5b7f1b7f8174a9003d467ff5122d280f"
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(
        body="following message was encrypted : "+plaintext,to="+16825524196",from_="+16823074500",)
    print(message.sid)
    print("Work done")
