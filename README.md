Lando project!

To install, from Ubuntu 18.04:

> sudo apt install python3-pip
> pip3 install virtualenv
> mkdir venv
> python3 -m virtualenv venv
> source venv/bin/activate

> pip install pip-tools
> pip-sync requirements.txt

To run app:
> ./serve.sh

To run tests:
> ./test.sh

