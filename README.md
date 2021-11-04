## Getting Started

This section is mainly focused on how you can get the project running on local, so you can use it only for development purposes. 

First, you need to install Django in you virtual environment

```bat
pipenv install django
pipenv install mysqlclient
```

Since we are gonna be using MySQL for this particular project, you should create an shema for the project's database.

```bat
create database lol_challenge;
create user loladmin identified by 'lolpwd';
grant all on lol_challenge.* to 'loladmin'@'%';
flush privileges;
```

Now to get into the environment for this project, and set up the directories that are basic.

```bat
pipenv shell
python manage.py makemigrations
python manage.py migrate
```

Finally, to run the actual project you just need to run.

```bat
python manage.py runserver
```

Then the page should be running in your local host in the port 8000 by default. 