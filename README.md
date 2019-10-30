# shroompred

Requires ubuntu

# Python3

Install Python 3

# Get pip

curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo python3

# Install Virtual Env

pip install --user virtualenv

# Create Virtual Environment

[If running a Unix-based VM on a Windows host, browse to a Linux filesystem if you are in a shared folder of Windows origin]

python3 -m virtualenv shroompred_app

# Activate your virtual environment

Based on the above location, activate virtual environment

source shroompred_app/bin/activate

# Install required packages

pip install -r requirements.txt

# Launch server

unzip web2py_src.zip
python3 web2py/web2py.py

# Type password
'admin' as password

You should get a browser launched
