from twilio.rest import TwilioRestClient
def CallHelp(toPhone,fromPhone):
    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACebd064fa9348992fc4e79ca4640381e2"
    AUTH_TOKEN = "5b7f1b7f8174a9003d467ff5122d280f"
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    call = client.calls.create(to=toPhone, from_=fromPhone,url="http://foo.com/call.xml")
    # print(call.length)
    # print(call.sid)
    print("Call completed")
