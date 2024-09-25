from twilio.rest import Client

def send_sms(phone_number, code):
    account_sid = 'ACf50fef9f49e2c6e00d3bf9377504132b'
    auth_token = 'ddbda3d79db00f2d76964ff39b4ce31d'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"Your verification code is {code}",
        from_='+1234567890',
        to=phone_number
    )
    return message
