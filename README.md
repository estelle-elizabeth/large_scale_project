# Large Scale Project
You need Django and postgresql.

you need to install postgres which should generate default username:postgres and password:1234

you will need to go to setting.py in mysite directory to link database to django. 

for that, you need database in postgres

go to cmd and type psql -U postgres. Then type in password to log in to postgres

then follow the code

CREATE DATABASE food;

\c food

create table user_truck;

create table truck;

now you have database and table. You can populate in django shell 

link to database settings: https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-DATABASES



I followed django tutorial from https://docs.djangoproject.com/en/2.2/intro/tutorial01/

there are only two tables that we are using. user_truck and truck in models.py inside polls directory

once you download the files, get to directory which has manage.py and run 'python manage.py shell' in command line.
you can populate tables from here 

The database will be empty so you need to populate. (you can find how to do so in the tutorial website on tutorial02)

python manage.py runserver will allow you to open websites in localhost 






