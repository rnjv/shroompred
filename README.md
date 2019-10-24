# shroompred

# Get pip

curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo python

# Install Virtual Env

pip install --user virtualenv

# Create Virtual Environment

[If running a Unix-based VM on a Windows host, browse to a Linux filesystem if you are in a shared folder of Windows origin]

python3 -m venv shroompred_app

# Activate your virtual environment

Based on the above location, activate virtual environment

source shroompred_app/bin/activate

# Install required packages

pip install -r requirements.txt

# Launch server

unzip web2py_src.zip


