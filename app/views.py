from flask import render_template
from app import app

from flask import Flask
from flask import request
from flask import url_for
from flask import flash
from flask import redirect

import socket
import geoip2.database

app = Flask(__name__)
from app import views


@app.route('/', methods=('GET', 'POST'))
def index():

	# This reader object should be reused across lookups as creation of it is
	# expensive.
	

	messages = []

	if request.method == "POST":
		ip = request.form['ip']

		
		# according socket.inet_aton method documentation
		# examples such as '1' and '1.555' can be 
		# as valid IPs. The former condition
		# compensates for this.
		try:
			if ip.count(".") == 3 and socket.inet_aton(ip):
				messages.append({'status': "Success", 'message': "Valid IP"})

				with geoip2.database.Reader('./app/static/GeoLite2-City.mmdb') as reader:
				    response = reader.city(ip);

				messages.append({'status': "Data", 'message': "Latitude: {}, Longitude: {} ".format(response.location.latitude, response.location.longitude)})

				return render_template("index.html", messages=messages)
			else:
				# invalid ip, return 400
				messages.append({'status': "Failure", 'message': "Please enter a valid IP."})
				return render_template("index.html", messages=messages)
		except:
			messages.append({'status': "Failure", 'message': "Please enter a valid IP."})
			return render_template("index.html", messages=messages)
	else:
		return render_template("index.html")
