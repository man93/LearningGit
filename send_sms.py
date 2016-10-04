from twilio.rest import TwilioRestClient
client = TwilioRestClient("Your account_id which u will get after account creation", "your authentication_id that you will get by twilio after account creation")
for i in range(1,4):
                client.messages.create(to="Number Whom you want to send the msg", from_="Your number provided by twilio after number verification", 
                       body="Msg that you want to give")
