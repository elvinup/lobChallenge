import lob
import urllib.parse
import requests
import json

civicKey = 'AIzaSyDxnEQ6T8FOdxjnFAC7xGp1q8ZNA3kKrjc'

#Grab from letter information and return as dictionary
def userInfo():
	'''
	fromName = input("Enter your full name: ")
	fromAddr1 = input("Enter your address: ")
	fromAddr2 = input("Enter your address line 2 or press enter: ")
	fromCity = input("Enter your City: ")
	fromState = input("Enter your state: ")
	fromZip = input("Enter your zip: ")
	message = input("Enter the message you'd like to send to a local representative: ")
	'''

	fromName = 'Elvin Uthuppan'
	fromAddr1 = '2001 Emmett Ct'
	fromAddr2 = ''
	fromCity = 'Valparaiso'
	fromState = 'IN'
	fromZip = '46385'
	message = 'ay waddup'
	
	#This will be the address dictionary useful later for creating the message
	fromAddress = {
		'name': fromName,
		'a1': fromAddr1,
		'a2': fromAddr2,
		'city': fromCity,
		'state': fromState,
		'zip': fromZip
	}
	
	addressUrl = fromAddr1 + ' ' + fromAddr2 + ' ' + fromCity + ' ' + fromState
	urlVars = {
		'key': civicKey,
		'address': addressUrl,
		'includeOffices': 'true',
		'roles': 'headOfGovernment',
		'levels': 'administrativeArea1' 
	}
	url = 'https://www.googleapis.com/civicinfo/v2/representatives?'
	
	googleUrl = url + urllib.parse.urlencode(urlVars)

	return fromAddress, googleUrl, message

#This will extract the json from the response and use the Lob API to create a letter 
def responseHandling(url):
	response = requests.get(url)
	data = response.json()
	print(data)
	

def main():
	address, url, msg = userInfo()
	responseHandling(url)
main()
