# Bank_API

# Setup

* running on Windows 10
* [Python 3.6.3](https://www.python.org/downloads/) installed
* clone this repo
* create a virtual environment and install required packages
```
C:\Bank_API>mkdir virtual_env
C:\Bank_API>python -m venv virtual_env
C:\Bank_API>virtual_env\Scripts\activate.bat
(virtual_env) C:\Bank_API>pip install -r requirements.txt
```

# Build

```
(virtual_env) C:\Bank_API>set FLASK_APP=bank.py
(virtual_env) C:]Bank_API>flask initdb
```

# Run

```
(virtual_env) C:\Bank_API>flask run
```

Open a new command line while the flask app is running and test using curl, similar to the examples below.

# Examples

*Get*

*Put*
```
C:\Bank_API>curl -X PUT "http://127.0.0.1:5000/api/marcia12?param=home_phone&value=3827948372"
{
    "record_id": 3,
    "username": "marcia12",
    "name": "Marcia Fredrickson",
    "mailing_address": {
        "street": "42 Kralltown Rd",
        "city": "Kralltown",
        "state": "PA",
        "zipcode": "17019"
    },
    "home_phone": "3827948372",
    "mobile_phone": "8392814932",
    "email_address": "marcia12@example.com"
}

C:\Bank_API>
```
```
C:\Bank_API>curl -X PUT -g "http://127.0.0.1:5000/api/marcia12?param=mailing_address&value={'street':'42+Kralltown+Rd','city':'Kralltown','state':'PA','zipcode':'17019'}"
{
    "record_id": 3,
    "username": "marcia12",
    "name": "Marcia Fredrickson",
    "mailing_address": {
        "street": "42 Kralltown Rd",
        "city": "Kralltown",
        "state": "PA",
        "zipcode": "17019"
    },
    "home_phone": "3827948372",
    "mobile_phone": "8392814932",
    "email_address": "marcia12@example.com"
}

C:\Bank_API>
```