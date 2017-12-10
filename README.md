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

Run curl in a separate command line, similar to the examples below.

# Examples

**Get**

*Profile*
```
C:\Bank_API>curl http://127.0.0.1:5000/api/leah223
{
    "record_id": 2,
    "username": "leah223",
    "name": "Leah Bradly",
    "mailing_address": {
        "street": "810 Main Street",
        "city": "York",
        "state": "PA",
        "zipcode": "17118"
    },
    "home_phone": "3829428391",
    "mobile_phone": "",
    "email_address": "leah223@example.com"
}
```
```
C:\Bank_API>curl http://127.0.0.1:5000/api/cate38
{
    "record_id": 1,
    "username": "cate38",
    "name": "Cate Watkins",
    "mailing_address": {
        "street": "374 Main Street",
        "city": "Dillsburg",
        "state": "PA",
        "zipcode": "17019"
    },
    "home_phone": "",
    "mobile_phone": "6578347234",
    "email_address": "cate38@example.com"
}
```
```
C:\Bank_API>curl http://127.0.0.1:5000/api/marcia12
{
    "record_id": 3,
    "username": "marcia12",
    "name": "Marcia Fredrickson",
    "mailing_address": {
        "street": "773 Temple Rd",
        "city": "New Haven",
        "state": "CT",
        "zipcode": "01132"
    },
    "home_phone": "",
    "mobile_phone": "8392814932",
    "email_address": "marcia12@example.com"
}
```

*Invalid Profile*
```
C:\Bank_API>curl http://127.0.0.1:5000/api/fake_username
{
    "status": 400,
    "message": "fake_username doesn't exist in the database"
}
```

*Savings*
```
C:\Bank_API>curl http://127.0.0.1:5000/api/savings/cate38
{
    "record_id": 1,
    "username": "cate38",
    "description": "savings account for cate38",
    "balance": 1000.42,
    "last_activity": "12/10/2017"
}
```

*Checking*
```
C:\Users\Bri\Desktop\Bank_API>curl http://127.0.0.1:5000/api/checking/marcia12
{
    "record_id": 3,
    "username": "marcia12",
    "description": "checking account for marcia12",
    "balance": 582.11,
    "last_activity": "12/10/2017"
}
```
```
C:\Bank_API>curl http://127.0.0.1:5000/api/checking/leah223
{
    "record_id": 2,
    "username": "leah223",
    "description": "checking account for leah223",
    "balance": 3829.33,
    "last_activity": "12/10/2017"
}
```

*Loan*
```
C:\Bank_API>curl http://127.0.0.1:5000/api/loan/leah223
{
    "record_id": 2,
    "username": "leah223",
    "description": "loan for leah223",
    "balance": 1000.0,
    "last_activity": "12/10/2017",
    "payment_due_date": "12/10/2025",
    "minimum_amount_due": 500.0
}
```

**Put**

*Modify Address*
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
```

*Modify Home Phone*
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
```

*Modify Mobile Phone*
```
C:\Bank_API>curl -X PUT "http://127.0.0.1:5000/api/cate38?param=mobile_phone&value=3294297481"
{
    "record_id": 1,
    "username": "cate38",
    "name": "Cate Watkins",
    "mailing_address": {
        "street": "374 Main Street",
        "city": "Dillsburg",
        "state": "PA",
        "zipcode": "17019"
    },
    "home_phone": "",
    "mobile_phone": "3294297481",
    "email_address": "cate38@example.com"
}
```

*Invalid Phone*
```
C:\Bank_API>curl -X PUT "http://127.0.0.1:5000/api/cate38?param=mobile_phone&value=4297481"
{
    "status": 400,
    "message": "Param mobile_phone or value 4297481 is invalid"
}
```

# Errors

* Certificates can't be added to the database or requested
* Valid emails are marked as invalid