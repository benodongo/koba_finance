import africastalking

# Initialize SDK
username = "tathmini2021"   
api_key = "b945348ca43b8e9550b3bacec94e52299e4080d3395e7f2acd386ffcaeff0e66"     
africastalking.initialize(username, api_key)

sms = africastalking.SMS

class send_sms():

    def send(self):
        # Set the numbers in international format
        recipients = ["+254705361244"]
        # Set your message
        message = "Hello, Reply with 1 to take part in this survey!"
        # Set your shortCode or senderId
        sender = "20880"
        try:
            response = sms.send(message, recipients, sender)
            print (response)
        except Exception as e:
            print (f'Error, we have a problem: {e}')