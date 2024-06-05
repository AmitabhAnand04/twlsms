from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Print the entire request for debugging purposes
    print('Incoming request:')
    print(request.values)
    
    # Get the message the user sent
    body = request.values.get('Body', None)
    number = request.values.get('From', None)  # assuming 'From' contains the sender's number

    # Log the incoming message
    print(f'Body = {body}')
    print(f'From = {number}')

    # Determine the right reply for this message
    if body == 'hello':
        reply_text = "User Admin login OTP is ** - SMSCNT"
    elif body == 'bye':
        reply_text = "User Admin login OTP is ** - SMSCNT"
    else:
        reply_text = "User Admin login OTP is ** - SMSCNT"

    # Send reply using SMS Country
    send_sms(reply_text, number)

    return "Message processed"

def send_sms(text, number):
    url = "https://restapi.smscountry.com/v0.1/Accounts/YhfYvqJjC8iAgjvxgNYi/SMSes/"
    payload = json.dumps({
        "Text": text,
        "Number": number,
        "SenderId": "SMSCNT",
        "DRNotifyUrl": "https://www.domainname.com/notifyurl",
        "DRNotifyHttpMethod": "POST",
        "Tool": "API"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic WWhmWXZxSmpDOGlBZ2p2eGdOWWk6QU1tUmlwUUhGNWlwdnkxaG9VRk1kRUp2NTd4TldCdWdSUXhTUDY1cg=='
    }

    response = requests.post(url, headers=headers, data=payload)
    print('SMS Country response:')
    print(response.text)

if __name__ == "__main__":
    app.run(debug=True)
