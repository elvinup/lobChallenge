# Letter To Representative

This project uses the command line to collect a user's information with Python and creates a link to a PDF of a letter to a US representative using that information. This is achieved using the Google Civic Information API to find a nearby representative and the Lob API is used to create the letter. 

### Prerequisites

Python 3

Run these commands as well to import these libraries if not already installed

```
pip install lob
pip install requests
```

### Files Needed

```
apiKeys.txt (First Line: Google Civic API key, Second Line: Lob API key)

letterToRep.py

README.md
```

### Example: 

The user will need to input their name, address, and message they would like to send to the representative

The output will contain a link to the letter. From here, right click the link and click open to be directed to a pdf of the letter on your default web browser.

## Command steps at a linux terminal:

```
python3 letterToRep.py

Enter your full name: <Your name>
Enter your address: <Your Street Address>
Enter your address line 2 or press enter: <Optional address 2>
Enter your City: <Your City>
Enter your state: <Your State> 
Enter your Zip Code: <Your zip code>
Enter your Country: <Your country> 
Enter the message you'd like to send to a local representative: <Any message>
``` 
Right click the URL below and open to get your letter!

[Link to letter PDF]

Thank you for the opportunity to apply by using Lob's actual API! 
