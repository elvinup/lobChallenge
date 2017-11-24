import lob
import urllib.parse
import requests
import json

#Grabs user information and returns it as a dictionary for from_address, the url, and the message 
def userInfo(civicKey):
	fromName = input("Enter your full name: ")
	fromAddr1 = input("Enter your address: ")
	fromAddr2 = input("Enter your address line 2 or press enter: ")
	fromCity = input("Enter your City: ")
	fromState = input("Enter your state: ")
	fromZip = input("Enter your zip: ")
	fromCountry = input("Enter your country: ")
	message = input("Enter the message you'd like to send to a local representative: ")
	print()	
	
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
	
	#Gets response from url requests and puts JSON into a readable dictionary	
	response = requests.get(url)
	civicResponse = response.json()
	
	try: 
		toAddress = {
			'name': civicResponse['officials'][0]['name'],
			'address_line1' : civicResponse['officials'][0]['address'][0]['line1'],
			'address_state' : civicResponse['officials'][0]['address'][0]['state'],
			'address_city' : civicResponse['officials'][0]['address'][0]['city'],
			'address_zip' : civicResponse['officials'][0]['address'][0]['zip']
		}
	
	except Exception as e: 
		return "There was a problem finding a representative with that information.\n Please try again"
	
	#Checks for address line 2 and puts an empty placeholder otherwise
	if 'line2' in civicResponse['officials'][0]['address'][0]:
		toAddress['address_line2'] = civicResponse['officials'][0]['address'][0]['line2']
	else:
		toAddress['address_line2'] = ""

	return toAddress

#Uses Lob API to create letter
def lobLetter(fromAddress, toAddress, msg, lobKey):
	
	lob.api_key = lobKey	

	try: 
		letter = lob.Letter.create(
			description = "Letter to Representative",
			to_address = toAddress,
			from_address = fromAddress,
			file = '<html style="padding-top: 3in; margin: .5in;">Dear Mr. \
			{{toName}},<br><br>{{message}}<br><br>Sincerely,<br>{{fromName}}</html>',
			merge_variables = {
				'toName': toAddress['name'],
				'message': msg,
				'fromName': fromAddress['name']
			
			},
			color = True	
			)
	
	except Exception as e: 
		return "An error occurred while making your letter. Please try again"	

	return letter["url"]

def main():

	keyFile = open('apiKeys.txt', 'r')
	keys = keyFile.read().split('\n')
	keyFile.close()	
	
	#Get the from_address content	
	fromAddress, url, msg = userInfo(keys[0])

	#Get the to_address content
	toAddress = responseHandling(url)

	#Use Lob API to retrieve a link to the letter
	letterUrl = lobLetter(fromAddress, toAddress, msg, keys[1])
	
	print("Right click the URL below and open to get your letter!\n")	
	print(letterUrl)
main()
