
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














2. ### Creating and setting up AWS:

1. Did the necessary sign up in [Amazon](https://aws.amazon.com/), created account and enter created to enable me use the platform, although it was not charged 
    * After email verification, logged into my aws console: 
    * Searched and opened s3: created a new bucket and added the appropriate user's groups and security policies for it.
    which will host my static and media files after deployment to heroku
    * While creating the bucket on S3, the public access checkboxe was switched off to allow access for users.
2. Clicking on properties which enable the Static Website Hosting option;
    * the input an index.html and error.html were entered into their appropriate fields
    * The bucket Permissions was created 
    * Clicked the CORS configuration which has a default prefilled config, and the needed code was insterted and saved.
3. Next the bucket policy was set to allow access to contents across the web 
    * Then amazon IAM was clicked to allow identity and access management of our stored files and folder. 
    * Still inside the IAM service; new group was created for our application and then we set the policies to ALL and then generates a downlaodable zip file containing ID and KEY to be used in the newly added group. 
    * This ID and KEY were stored as environment variable heroku config.
4. To connect django with the aws bucket:
    * pip3 install boto3
    * pip3 install django-storages
    * pip3 freeze >requirements.txt
    * settings.py : added django-storages to installed apps
    * settings.py: added an if statement to check if on heroku, it should use the aws bucket that will provide the bucket settings
    * From here, django will collectstatic files automatically and upload them to s3.
    * A custom storage class was created using s3boto3 storage class from django storages: to tell django to
    use s3 to store  static files in production when collectstatic is ran or uploads any image. The should save both the static and media files.
5. It is important to note that:nthis command has to be run in the development(local) environment each time change is made in the static files/folder. This will enable the folder and files saved to AWS S3 bucket.



*The project need to be clone locally through the following steps:*

1. Browse the repository link [Greenery Equipment](https://github.com/Rozdandy/greenery_equipment) to clone the project by clicking the green Clone or download button and downloading the project to local computer and extracting it.
2.  Or by entering the following into the Git CLI terminal: https://github.com/Rozdandy/africadelishms3.git
3.	Open Githpod workspace, that is Git Bash.
2. Open your Terminal : ensure that your current working directory is the location you want the clone directory to be in
3. git clone : paste in the HTTPS url you copied
4. ensure to check the requirements.txt for all the necessary dependencies you will need to install for the project

   Use the following envronment variable

    | Env Variable          | Value                      | Location      
    |-----------------------|----------------------------|-----------------|
    | DATABASE_URL          | your postgres url          | heroku          |
    | DEVELOPMENT           | True                       | gitpod          |
    | SECRET_KEY            | your django secret_key     | gitpod & heroku |
    | STRIPE_PUBLIC_KEY     | your stripe public key     | gitpod & heroku |
    | STRIPE_SECRET_KEY     | your stripe secret key     | gitpod & heroku |
    | STRIPE_WH_SECRET      | your stripe webhook secret | gitpod & heroku |
    | AWS_ACCESS_KEY_ID     | your aws access key        | gitpod & heroku |
    | AWS_SECRET_ACCESS_KEY | your aws secret access key | gitpod & heroku |
    | EMAIL_HOST_PASS       | your gmail host pass       | gitpod & heroku |
    | EMAIL_HOST_USER       | your gmail host user       | gitpod & heroku |
    | USE_AWS               | True                       | heroku          |                   

6.  Navigate to the correct file location after unzipping the files and cd <path to folder>
5. for further info on github cloning : [Github](https://docs.github.com/en/enterprise/2.13/user/articles/cloning-a-repository).