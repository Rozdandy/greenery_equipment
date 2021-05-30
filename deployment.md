
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
