# ESSY.me

Website built using Django + React via webpack.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Installing

Install React/Node dependencies
```
npm install
```
Install python dependencies
```
pip install
```

### Running locally

Start the django server

```
python manage.py runserver
```

local db login

```
username: admin
password: developer password
```

run the --watch command on webpack to auto generate new bundle.js files when changes are detected in your code.  Terminal command located in package.json.

```
npm start
```
manually compile JavaScript files with

```
npm pack
```

Start a Grunt watcher to compile LESS to CSS when changes are detected

```
grunt
```
----------------------------------------------------------------------------
To connect to gcloud cloud SQL client, run this

```
gcloud auth login
gcloud config set project <PROJECT_ID>
gcloud sql instances describe <INSTANCE_NAME>
```

Initialize gcloud Cloud SQL instance (hint: you will need the 'cloud_sql_proxy' exec file)

```
./cloud_sql_proxy -instances="essy-178102:us-central1:essy-db"=tcp:5432
```

This step establishes a connection from your local computer to your Cloud SQL instance for local testing purposes.

----------------------------------------------------------------------------
Write google app default credentials
```
gcloud auth application-default
```

Copy all local static folder cloud storage static folder
```
gsutil rsync -R static/ gs://essy/static
```


---- DEPLOY APP ----
```
gcloud app deploy
```

DEBUG APP
```
gcloud app --project [PROJECT-ID] instances enable-debug
gcloud app --project [PROJECT-ID] instances disable-debug

```
