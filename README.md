# MoniNag
**MoniNag** is a monitoring system that performs server monitoring. MoniNag offers monitoring, 
alerting user via Email and visualized statistics for servers. The system provides highly 
customizable approach towards monitoring.

## Installation
We are assuming that you're using bash & you have to install or clone such packages:

* Install PostgreSQL server on local machine

  ```
  sudo apt-get install postgresql postgresql-contrib
  sudo apt-get install python-psycopg2
  sudo apt-get install libpq-dev
  ```
* Install RRD tool on local machine
 
  ```
  sudo apt-get install librrds-perl librrd-dev rrdtool
  ```
* Clone this repository to your local machine
  
  ```
  git clone https://github.com/Lv-219-Python/MoniNag.git
  ```
* Go to the local copy of repository. Open terminal and run the following command
  
  ```
  pip install -r moninag/requirements.txt
  ```
* Create your *local_settings.py* in the folder with *settings.py* and configure it 
  * Database settings
    
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': database_name,
            'USER': database_username,
            'PASSWORD': user_password,
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
    ```
  * Email settings
  
      ```
      ACCOUNT_ACTIVATION_DAYS=7
      EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
      EMAIL_PORT=587
      EMAIL_HOST = 'smtp.gmail.com'
      EMAIL_HOST_USER = 'moninaginfo@gmail.com'
      EMAIL_HOST_PASSWORD = '1234rewqasdfvcxz'
      EMAIL_USE_TLS = True
      DEFAULT_FROM_EMAIL = "moninaginfo@gmail.com"
      WSGI_APPLICATION = 'moninag.wsgi.application'
      DEFAULT_HOST = 'localhost:8000'
      ```
* Install npm and packages
 
  ```
  curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
  sudo apt-get install -y nodejs
  sudo npm install webpack -g
  sudo npm install typescript -g
  npm i
  webpack --watch
  ``` 
* Install nagios-plugins on local machine
 
  ```
  sudo apt-get install nagios-plugins
  ```

## Tests
* Back-end Unit Tests for entire project are in **tests/unittests/** directory. In order to launch 
tests use:

    ```
    python manage.py test
    ```
* For test effectiveness estimation our team used **coverage py**. Main configuration for 
coverage are in **.coveragerc** config file where you can customize run/report/html/... sections.
In order to omit some file or directory which is not intented to be covered with tests add them 
in **[run]** section:

    ```
    omit = filename.py
    ```
    
    In order to run coverage use:
    ```sh
    coverage run manage.py test
    ```
    
    To get report output you can store it in html/xml or simply print it into console:
    ```sh
    coverage report 
    coverage report html
    coverage report xml
    ```
    
    More information at [Coverage](https://coverage.readthedocs.io/en/coverage-4.3.4/)
   

## Other
* Code Convention. For analyzing and establishing clean code (according to PEP8) we use **pylint**. 
In addition since project uses Django **pylint_django** plugin for pylint is used. All pylint 
configurations are in **.pylintrc** config file. To check specific  file or package use:
  
    ```sh
    pylint --rcfile=/path/.pylintrc filename.py
    ```
    Additional information: [Pylint User Manual](https://pylint.readthedocs.io/en/latest/)