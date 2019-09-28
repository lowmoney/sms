from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from ggScrapper import search

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():

	# Get the sms body
	body = request.values.get('Body',None)
	
	# Start our response
	resp = MessagingResponse()

	# Add a message
	items = search(str(body))
	for i in range(0,len(items[0])):
		resp.message(items[0].pop() + ": " + items[1].pop() + " at " + items[2].pop())

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)
