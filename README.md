# Bank_API

# Setup

* running on Windows 10
* [Python 3.6.3](https://www.python.org/downloads/) installed
* clone this repo
* create a virtual environment and install required packages
```
Bank_API>mkdir virtual_env
Bank_API>python -m venv virtual_env
Bank_API>virtual_env\Scripts\activate.bat
(virtual_env) Bank_API>pip install -r requirements.txt
```

# Build

```
(virtual_env) Bank_API>set FLASK_APP=bank.py
(virtual_env) Bank_API>flask initdb
```

# Run

```
(virtual_env) Bank_API>flask run
```

Open a new command line while the flask app is running and test using curl, similar to the examples below.

# Examples

*Get*

