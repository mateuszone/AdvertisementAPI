# Advertisment REST API

#### Simple REST app for advertisment

#### Written with:
##### Python 3.8
##### Djangorestframework 3.12.4
##### Django 3.2.6

# Installation

#### Install with pip:

`$ pip install -r requirements.txt`


#### Create db and make some migrations in terminal

`python3 manage.py makemigrations`

`python3 manage.py migrate`

#### Create superuser to enter admin panel

`python3 manage.py createsuperuser`

#### Enter some data to db in admin panel

#### Run Docker

##### In repository you have files: Dockerfile and docker-compose.yml.

##### Build and run server with app:

`$ docker-compose up -d`

##### Stop sever:

`$ docker-compose down`

## API url's 
#### Show list of available urls

### Category

##### These urls allow everyone to make all crud operations without registration. 
##### On this url you can set ordering by name field (asc or desc).

`[GET] /api/category/`

`[POST] /api/category/`

`[PUT] /api/category/{category.id}/`

`[DELETE] /api/category/{category.id}/`

### Offers

##### These urls allow everyone to make all crud operations without registration. 
##### On this url you can enter additional query parameter "category" after ? to retrieve only records within specified category

`[GET] /api/offers/`

`[POST] /api/offers/`

`[PUT] /api/offers/{offer.id}/`

`[DELETE] /api/offers/{offer.id}/`

### Tests
#### To run simple test type in terminal:

`python manage.py test`