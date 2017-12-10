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
(virtual_env) C:\Bank_API>flask initdb
```

Creates three users in the database (cate38, leah223, and marcia12) each wih one savings account, one checking account, one loan, and one certificate each

# Run

```
(virtual_env) C:\Bank_API>flask run
```

Run curl in a separate command line, similar to the examples below.

# Examples

**Get**

*Profile*
```
C:\Bank_API>curl http://localhost:5000/api/leah223
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
C:\Bank_API>curl http://localhost:5000/api/cate38
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
C:\Bank_API>curl http://localhost:5000/api/marcia12
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
C:\Bank_API>curl http://localhost:5000/api/fake_username
{
    "status": 400,
    "message": "fake_username doesn't exist in the database"
}
```

*Savings*
```
C:\Bank_API>curl http://localhost:5000/api/savings/cate38
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
C:\Users\Bri\Desktop\Bank_API>curl http://localhost:5000/api/checking/marcia12
{
    "record_id": 3,
    "username": "marcia12",
    "description": "checking account for marcia12",
    "balance": 582.11,
    "last_activity": "12/10/2017"
}
```
```
C:\Bank_API>curl http://localhost:5000/api/checking/leah223
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
C:\Bank_API>curl http://localhost:5000/api/loan/leah223
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

*Certificate*
```
C:\Bank_API>curl http://localhost:5000/api/certificate/cate38
{
    "record_id": 1,
    "username": "cate38",
    "description": "certificate for cate38",
    "balance": 1000.0,
    "last_activity": "12/10/2017",
    "interest_rate": 0.05,
    "maturity_date": "12/10/2032"
}
```

*Invalid Certificate*
```
C:\Bank_API>curl http://localhost:5000/api/certificate/fake_username
{
    "status": 400,
    "message": "Certificate doesn't exists under fake_username"
}
```

**Put**

*Modify Address*
```
C:\Bank_API>curl -X PUT -g "http://localhost:5000/api/marcia12?param=mailing_address&value={'street':'42+Kralltown+Rd','city':'Kralltown','state':'PA','zipcode':'17019'}"
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
C:\Bank_API>curl -X PUT "http://localhost:5000/api/marcia12?param=home_phone&value=3827948372"
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
C:\Bank_API>curl -X PUT "http://localhost:5000/api/cate38?param=mobile_phone&value=3294297481"
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
C:\Bank_API>curl -X PUT "http://localhost:5000/api/cate38?param=mobile_phone&value=4297481"
{
    "status": 400,
    "message": "Param mobile_phone or value 4297481 is invalid"
}
```

*Invalid Address*
```
C:\Bank_API>curl -X PUT -g "http://localhost:5000/api/marcia12?param=mailing_address&value={'street':'42+Kralltown+Rd','city':'Kralltown','state':'PA','zipcode':''}"
{
    "status": 400,
    "message": "Param mailing_address or value {'street': '42 Kralltown Rd', 'city': 'Kralltown', 'state': 'PA', 'zipcode': ''} is invalid"
}
```

# Errors and Improvements

* All emails are marked as invalid, even if they're not.
* Duplication could be improved by creating a universal to_dict() method instead of individual, repeated, to_dict() methods in every model.
* Savings, Checking, Loan, and Certificate models could extend from a more generic structure to reduce repeated information.
* The type of endpoint to return (Savings, Checking, Loan, or Certificate) could be passed as a parameter in the request so that there doesn't need to be a class and get method for each endpoint, just one get method that takes the passed in structure parameter to know which account to return.
