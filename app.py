from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def incoming_sms():
    """Handle incoming SMS messages"""
    # Log the entire request for debugging purposes
    print('Incoming request:')
    print(request.values)
    
    # Accessing form data
    mn = request.values.get('mn')
    msg = request.values.get('msg')
    
    # Process the data as needed
    print("Mobile number:", mn)
    print("Message:", msg)
    
    # Return a 200 OK response code
    return jsonify({'status': 'Message received'}), 200

if __name__ == "__main__":
    app.run(debug=True)
