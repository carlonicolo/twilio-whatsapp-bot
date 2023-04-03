import coinmarket as coin
from flask import Flask
from flask import request
from twilio.rest import Client
import os
app = Flask(__name__)

ACCOUNT_ID = os.environ.get('TWILIO_ACCOUNT')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
client = Client(ACCOUNT_ID, TWILIO_TOKEN)
TWILIO_NUMBER = 'whatsapp:+14155238886'

def process_msg(msg):
    response = ""
    if msg == "hi":
        response = "Hello, welcome to the crypto currency BOT. Write value <crypto-name> <currency> to return the value of crypto name in the currency passed.\n Example value bitcoin USD!"
    
    elif "value" in msg:
        response = coin.getInfo((msg.split())[1], (msg.split())[2])
    
    else:
        response = "Please type hi to get started."
    return response


def send_msg(msg, recipient):
    client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to=recipient
    )

@app.route("/")
def hello():
    return {
        "Result":"You successfully created the first route!"
    }

    
@app.route("/webhook", methods=["POST"])
def webhook():
    # message = request.form["message"]
    # return {
    #     "Result": message
    # }
    
    # Using debugger to check what kind of values are in the request.form
    # in the console: 
    #   f = request.form
    #   f     
    # import pdb
    # pdb.set_trace()
    # return "OK", 200
    
    f = request.form
    msg = f['Body']
    sender = f['From']
    response = process_msg(msg)
    send_msg(response,sender)
    return "OK", 200
    