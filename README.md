# Advertisement REST API

## Overview
#### Simple REST API for advertisement app with all crud operations.

### Technology:

##### Python 3.8

##### Djangorestframework 3.12.4

##### Django 3.2.6

# Installation

#### Create python3.8 venv

#### Install with pip:

`$ pip install -r requirements.txt`

#### Create db and make some migrations in terminal. If you will not use docker and want to use sqlite3 db just comment out current DATABASE settings with postgre in settings.py and uncomment DATABASE with sqlite3 settings.
#### If you want to use postgres on local server you need to set up database settings in settings.py


`python3 manage.py migrate`

#### Create superuser to enter admin panel

`python3 manage.py createsuperuser`

##### To populate db to get more records use manage.py custom command "seed" in default it adds 10 records, but you can
##### set your own number of records:

`python3 manage.py seed`


## Run API with Docker

##### In repository, you have files: Dockerfile and docker-compose.yml.

##### create .env file in AdvertisementAPI catalog and copy of it in API catalog and add custom env variables to set up 
##### postgre db.

`POSTGRES_DB=type_your_db_name`
`POSTGRES_USER=type_your_username`
`POSTGRES_PASSWORD=type_your_password`

`sudo docker-compose build`

`sudo docker-compose up`

##### open another terminal window

`sudo docker ps`

##### copy id of the container-id with web in name and type below command:

`sudo docker exec -it conteinerid bash`

##### To populate db use:

`python3 manage.py migrate`

##### To populate db to get more records use manage.py custom command "seed" in default it adds 10 records, but you can set
##### your own number of records:

`python3 manage.py seed`

##### If you want to Stop sever:

`$ docker-compose down`

## API url's

#### Show list of available urls

### Category

##### These urls allow everyone to make all crud operations without registration.

##### On this url you can set ordering by name field (asc or desc).

`[GET] /api/category/`

`[GET] /api/category/{offer.id}/`

`[POST] /api/category/`

`[PUT] /api/category/{category.id}/`

`[DELETE] /api/category/{category.id}/`

### Offers

##### These urls allow everyone to make all crud operations without registration.

##### On this url you can enter additional query parameter "category" after ? to retrieve only records within specified category

`[GET] /api/offers/`

`[GET] /api/offers/{offer.id}/`

`[POST] /api/offers/`

`[PUT] /api/offers/{offer.id}/`

`[DELETE] /api/offers/{offer.id}/`

## Tests

#### To run simple test type in terminal:

`python manage.py test`