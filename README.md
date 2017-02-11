# MoniNag

## Install
We are assuming that you're using bash & you have to install or clone such packages:

* Install PostgreSQL server on local machine
  
  ```
  sudo apt-get install postgresql postgresql-contrib
  sudo apt-get install python-psycopg2
  sudo apt-get install libpq-dev
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
