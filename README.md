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
