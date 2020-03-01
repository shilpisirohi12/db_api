#command to install all the requirements

pip install -r requirements.txt

#install mysql client
pip install .\mysqlconnector\mysqlclient-1.4.6-cp37-cp37m-win32.whl


#setting environment

python -m venv .venv

.venv\scripts\activate

Ctr+shift+P and select Python Interpreter and then select with venv


#command to save all the requirements in the file

pip freeze > requirements.txt

