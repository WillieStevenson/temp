import pytest
import requests

def test_index_page():
	response = requests.get("http://localhost:5000/")
	assert response.status_code == 200
	assert b'Enter a valid IPv4 IP' in response.content
	assert b'Submit' in response.content

def test_input_strings():
	response = requests.post("http://localhost:5000/", data={'ip':'1.1.1.1'})
	assert b'Success' in response.content
