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

	return render_template("index.html")
