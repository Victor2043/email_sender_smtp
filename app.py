from flask import Flask
from email_sender_smtp import send_email

app = Flask(__name__)

@app.route('/', methods=['GET'])
def endpoint_test():
    return "Ok"

@app.route('/send_email/<email>', methods=['GET'])
def send_email_smtp(email):
    response = send_email(email)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=80)