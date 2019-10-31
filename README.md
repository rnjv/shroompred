# shroompred

Requires ubuntu

# Python3

Install Python 3 and Git (optional)

# Download or extract git repo

`git clone https://github.com/rnjv/shroompred.git` or unzip the given file.

`cd shroompred`

# Get pip

Linux:

`curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo python3`

Windows:

Download get-pip.py (https://bootstrap.pypa.io/get-pip.py) to a folder on your computer. Open a command prompt window and navigate to the folder containing get-pip.py. Then run python get-pip.py. This will install pip.

# Install Virtualenv

`pip install --user virtualenv`

# Create Virtual Environment

[If running a Unix-based VM on a Windows host, browse to a Linux filesystem if you are in a shared folder of Windows origin]

`python3 -m virtualenv shroompred_app`

# Activate your virtual environment

Activate virtual environment (working directory is shroompred, make sure you have cd into it as instructed above)

`source shroompred_app/bin/activate` (on Linux)

`shroompred_app/Scripts/activate` (on Windows)

# Install required packages

`pip install -r requirements.txt`

# Launch server

`unzip web2py_src.zip` (On Windows, be sure to unzip so that only the web2py folder is overwritten and no new foler is created)

`python3 web2py/web2py.py`

# Type password

'admin' as password

You should get a browser launched

# 
# Testing backend

`python3 web2py/web2py.py -M -S shroompred`

`import requests, json`

`#helper to generate random variables for request`
`varslist = gen_rest_varslist(short=1)`

`r = requests.get("http://127.0.0.1:8000/rest/api?short=1", data=json.dumps(varslist), headers={"content-type": "application/json"})`

`r.text`
