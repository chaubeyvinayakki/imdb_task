IMDB
=========

## Virtual Envirnoment and requirements

    virtualenv -p /path/to/python3.7 venv
    source venv/bin/activate
    pip install -r requirements.txt

## run migrations
   
   python manage.py migrate


## Run management command to populate data from json file

   python manage.py movies

## Running Development Server

    python manage.py runserver

## Routes used to search the movie info:
    To search movie by name : http://localhost:8000/api//movie-detail/?name=sholay
    To search movie by director name : http://localhost:8000/api//movie-detail/?director=sholay
    
## POSTMAN COLLECTION:
    please find below postman collection link of all api:
    https://www.getpostman.com/collections/777b3118b1c98dc72955
    
## Following are the ways to scale the architecture to handle million of request::
    1. Create replica of the database so that if one replica is down , so that data can be reteriv from from other replica.
    2. We can also create replica of the server so that if one server goes down request are transfered to the other replica.
    3. We can add throttling on server side to allow specific number of aunthenticated user can access the api.
    4. For search part we can also implement eastic search for the fast retreival of tha data, in django we can do this by using elasticsearch-dsl module.    
    5. We can add load blanacer on server.
    6. Split the services into micro services so that if one server goes down others will run.  