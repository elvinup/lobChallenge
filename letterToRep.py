import lob
import urllib.parse
import requests
import json

civicKey = 'AIzaSyDxnEQ6T8FOdxjnFAC7xGp1q8ZNA3kKrjc'
lob.api_key = 'test_0464d171713c005720c19315945b7000b1b'

#Grabs user information and returns it as a dictionary for from_address, the url, and the message 
def userInfo():
	'''
	fromName = input("Enter your full name: ")
	fromAddr1 = input("Enter your address: ")
	fromAddr2 = input("Enter your address line 2 or press enter: ")
	fromCity = input("Enter your City: ")
	fromState = input("Enter your state: ")
	fromZip = input("Enter your zip: ")
	fromCountry = input("Enter your country: ")
	message = input("Enter the message you'd like to send to a local representative: ")
	'''

	fromName = 'Elvin Uthuppan'
	fromAddr1 = '2001 Emmett Ct'
	fromAddr2 = ''
	fromCity = 'Valparaiso'
	fromState = 'IN'
	fromZip = '46385'
	fromCountry = 'US'
	message = 'ay waddup'
	
	#This will be the address dictionary useful later for creating the lob letter request
	fromAddress = {
		'name': fromName,
		'address_line1': fromAddr1,
		'address_line2': fromAddr2,
		'address_city': fromCity,
		'address_state': fromState,
		'address_zip': fromZip,
		'address_country': fromCountry
	}
	
	#Creates the custom url for the google civic API
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


#This will extract the json from the response and returns a the to_address field
def responseHandling(url):
	response = requests.get(url)
	
	#Puts the response data into a readable dictionary
	civicResponse = response.json()
	toAddress = {
		'name': civicResponse['officials'][0]['name'],
		'address_line1' : civicResponse['officials'][0]['address'][0]['line1'],
		'address_state' : civicResponse['officials'][0]['address'][0]['state'],
		'address_city' : civicResponse['officials'][0]['address'][0]['city'],
		'address_zip' : civicResponse['officials'][0]['address'][0]['zip']
	}

	#Checks for address line 2 and puts an empty placeholder otherwise
	if 'line2' in civicResponse['officials'][0]['address'][0]:
		toAddress['address_line2'] = civicResponse['officials'][0]['address'][0]['line2']
	else:
		toAddress['address_line2'] = ""

	return toAddress

def lobLetter(fromAddress, toAddress, msg):
		

def main():
	
	fromAddress, url, msg = userInfo()
	toAddress = responseHandling(url)
	lobLetter(fromAddress, toAddress, msg)

main()


