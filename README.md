# GER-TREK
### These are the voyages of the webapp GerTrek
### To boldy go where no code has gone before.
#### This readme is a stub and needs to be expanded along the way.

## Dependencies
+ python
+ python-virtualenv

## Setup
```shell
virtualenv -p /path/to/python2.7 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Commands
```shell
#initialize database and create superuser
./manage.py setup
#create migrational background
./manage.py db init
#start development server
./manage.py runserver
```

## Functionality
+ Provide possibility for members to write blogposts
+ Customize accessibilty to posts
+ Provide a map to track progress of trek
+ tbc
