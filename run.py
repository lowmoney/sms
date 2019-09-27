from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from ggScrapper import search
import pyshorteners
from pyshorteners import Shorteners

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():

	s = pyshorteners.Shortener(Shorteners.TINYURL)

	# Get the sms body
	body = request.values.get('Body',None)
	
	# Start our response
	resp = MessagingResponse()

	# Add a message
	items = search(body)
	for i in range(0,len(items[0])):
		resp.message(items[0].pop() + ": " + items[1].pop() + " at " + s.short(items[2]))

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)
