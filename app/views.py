from flask import render_template

from flask import Flask
from flask import request
from flask import url_for
from flask import flash
from flask import redirect

import socket
import geoip2.database

app = Flask(__name__)


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
		# See https://docs.python.org/3/library/socket.html#socket.inet_aton
		try:
			if ip.count(".") == 3 and socket.inet_aton(ip):
				messages.append({'status': "Success", 'message': "Valid IP"})

				with geoip2.database.Reader('./app/static/GeoLite2-City.mmdb') as reader:
				    response = reader.city(ip);

				messages.append({'status': "Data", 'message': "Latitude: {}, Longitude: {} ".format(response.location.latitude, response.location.longitude)})

				return render_template("index.html", messages=messages), 200
			else:
				messages.append({'status': "Failure", 'message': "Please enter a valid IP."})
				return render_template("index.html", messages=messages), 400
		except:
			messages.append({'status': "Failure", 'message': "Please enter a valid IP."})
			return render_template("index.html", messages=messages), 400
	else:
		return render_template("index.html")
