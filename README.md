## CANDY DELIVERY APP
REST API for Yandex school

This project presents the implementation of the Rest API service, which allows you to hire couriers to work, take orders and optimally distribute orders between couriers. The project was developed as part of the Yandex Backend Development School

## To start the project, you need to follow these steps:
1) Clone the project and go to the project folder (command 'git clone' with a link to the project)

2) If the server is already running, then run the command - 'killall python' or 'sudo kill -9 "process PID"' (PID can be found with the command 'sudo netstat -ltup')

3) Run the command 'bash start_server.sh' or 'make all' (if you run from a third-party VM, you will need to rewrite the path in start_server.sh)

4) Before using, you need to clear all the current tables that are in mysql in the candy_delivery_app database as follows:

5) Go to mysql (bash command - 'mysql')

6) Select database - 'use candy_delivery_app;'

7) Clear table - 'TRUNCATE TABLE order;' and 'TRUNCATE TABLE courier;'

8) Exit mysql ('exit')

After the first run, it is advisable to "comment out" db.create_all () in models.py, which is used purely to create tables in the database from classes.

The tests are in the tests.py file. They include both valid and invalid tests for all handlers, as well as tests that check the interaction of several handlers with each other (for example, canceling courier orders after updating its parameters, accounting for delivered orders when assigning new ones). Before each test, a comment is given containing brief information about the test (valid / invalid, what exactly is invalid, etc.), in addition, by the very name of the test-function, you can understand what the test is checking. The pytest library is designed in such a way that you can run the tests of interest separately, or you can run everything at once. Important: in order to check the interaction of handlers with each other, the database had to be filled with data (files: 'data_couriers.py', 'data_orders.py', import is implemented inside the file 'test.py' before 'complex' tests).

## The following libraries were used in the implementation:

Flask is a general structure,

flask_SQLAlchemy - for working with a database,

Datetime - for validating and saving dates,

requests - for working with HTTP requests;

pytest - for testing REST API service

To store the data, the Mysql database was used (When starting from a third-party computer, you need to create the 'candy_delivery_app' database, and rewrite the path to it in the config.py file)

## Project files

view.py - contains all necessary handlers (1: POST / couriers, 2: PATCH / couriers / $ courier_id, 3: POST / orders, 4: POST / orders / assign, 5: POST / orders / complete) and, accordingly, is responsible for all the commands of the Rest API service, in addition, in some handlers, input data validation is prescribed

validation.py - functions for validation

models.py - stores the Courier and Order classes

config.py - project configuration

app.py - primary declaration and database access

main.py - run the program

tests.py - contains tests with valid and invalid data / requests

start_server.sh - script for starting the server through gunicorn, it is it that starts the Virtual Machine on reboot
