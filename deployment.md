
# Deployment:

The deployment process was in two major steps and project cloning:
1. Deploying to Heroku
2. Creating and setting up AWS
3. Project cloning



1. ## Deploying to Heroku:
----
 Creating heroku app and linking to github repo:

1. Logg In to Heroku website [click here](https://dashboard.heroku.com/)
2. Clicked on create new app, gave it a name and specified my region
3. On Heroku dashbaord, clicked on resources and then add-ons, searched for Postgres database and provisioned the free version for my heroku app
4. To use Postgres back in gitpod, the following were installed using pip3 install: 
  * dj_database_url, 
  * psycopg2
  * psycopg2-binary
5. On gitpod terminal, the number (4) above were freezed using: pip3 freeze --local > requirements.txt: which installed all the necessary dependencies for the project
6. Setting up Postgres database on gitpod: 
    * settings.py: import dj_database_url
    * At the databases setting: the default configuration was temporarily commented out , and replaced it with a call to dj_database_url.parse()
    and give it the Postgres database URL from Heroku.
    * "python3 manage.py showmigrations" command was ran on gitpod terminal to show all the migration
    * "python3 manage.py migrate" command was ran to apply all those migrations and get my database all set up.
7. Importing all categories and products data that are inside fixture to postgres, that is, the new setup database:
    * At the databases setting, still inside settings.py:  I ensured that still on dj_database_url database
    "django.db.backends.sqlite3"
    * Ran the following commands at gitpod terminal to create fixtures: 
        - python3 manage.py loaddata category
        - python3 manage.py loaddata products 
8. setting-up superuser on Postgres: 
    * Gitpod terminal, used the command "python3 manage.py create superuser" to enable entrance to the admin of the project
9. Still inside Settings.py : I ensured that Postgres database is well connected to Heroku and gitpod use django.db.backends.sqlite3 for loc
10. Back on Gitpod terminal: unicorn was installed using the command "pip3 install gunicorn". This will act as my webserver
    * pip3 freeze --local > requirements.txt
    * Created Procfile : To tell Heroku to create a web dyno.Which will run unicorn and serve the django app.
    * On "heroku config: set Disable collectstatic=1"; collectstatic was disabled to prevent heroku from collecting static files.
11. At Settings.py: heroku app name was added to enable hosting
    * in my gitpod work environment CLI: $ heroku login : to login to heroku from my terminal
12. Gipod terminal: git add .
13. Gipod terminal: git commit -m "add all the changes"
14. Gipod terminal: git push -u heroku master






