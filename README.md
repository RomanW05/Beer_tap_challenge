# About this Challenge

Ever heard of self-service beer tap dispensers? These are a new concept of drink dispenser that is already being used in many international music festivals to avoid long queues and crowds.

The user brings his or her glass and self-serves the beer. The system registers the amount dispensed and calculates the price of the service, transferring this information to the bar counter. Great innovation, isn't it?

Well, for this challenge we propose you to develop the API that controls this system and calculates the price of the drinks for each attendee, based on the amount dispensed.


# How it works?

The aim of this API is to allow organizers to set up these bar counters allowing the attendees self-serving.

So, once an attendee wants to drink a beer (0,0º, we are not promoting any kind of alcohol consumption! 👀) they just need to open the tap! The API will start counting how much flow comes out and, depending on the price, calculate the total amount of money.

You could find the whole description of the API and send some requests to a mock server at <a href='https://rviewer.stoplight.io/docs/beer-tap-dispenser/juus8uwnzzal5-beer-tap-dispenser'>this URL</a>.


# Workflow

The workflow of this API is as follows:

1. Admins will create the dispenser by specifying a flow_volume. This config will help to know how much litres of beer comes out per second and be able to calculate the total spend

2. Every time an attendee opens the tap of a dispenser to puts some beer, the API will receive a change on the corresponding dispenser to update the status to open. With this change the API will start counting how much time the tap is open, and be able to calculate the total price later

3. Once the attendee closes the tap of a dispenser, as the glass is full of beer, the API receives a change on the corresponding dispenser to update the status to close. At this moment, the API will stop counting and mark it closed.

At the end of the event the promoters will want to know how much money they make with this new approach. So, we have to provide some information about how many times a dispenser was used, for how long, and how much money made with each service.