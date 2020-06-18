# Movie Rating API

MovieRating API is a Django, Celery based API that is used to add the movie and rate the movie by the token-based authenticated users and send the emails of the average rating to the owner of movies at a specific time per day.

## Installation

Install the below package and server before using API.

```bash
1. Install Redis-server and configure the port "6379" as the localhost. use below command to start redis-server.
    $ redis-server

2. Go to MovieRating/
3. run the following command to start the celery workers.
    $ celery -A MovieRating worker -l info

4. Run the following command to produce task periodically.
    $ celery -A MovieRating beat -l info

5. Run requirements.txt file to install all dependencies of API.
    $ pip install -r requirement.txt

6. run the migrations: 
    $ python manage.py makemigrations
    $ python manage.py migrate

7. insert dummy data:
    $ python MovieRating/SetupData.py

8. python
    $ python manage.py runserver





```

## Usage
1. Below instruction to use the API.

```bash
    User should be registered.
    User should have Token after login.
    Movie should be added before rating.
    Rating should be in range(1-5).
```
2. Below endpoints of API.

```
$ http://localhost:8000/Api/register
  * Method -> POST
  * Url params
           username[String]
           password[String]
           email[String]
  * Success Response
           Status - 200
           Content - {'Message' : 'User created successfully.'}
           
  * Error Response 
           Status - 400
           Content - {'error': 'user already exist'}

           Status - 400
           Content - {'error': 'username, password & email are required but not provided'}

$ http://localhost:8000/Api/login 
  * Method -> POST
  * Url params
           username[String]
           password[String]
  * Success Response
           Status - 200
           Content - {'token': token}
           
  * Error Response 
           Status - 400
           Content - {'error': 'Invalid Credentials'}

           Status - 400
           Content - {'error': 'Please provide both username and password'}

$ http://localhost:8000/Movie/movieadd
  * Method -> POST
  * headers:
        Authorization: Token

  * Url params
           movie[String]

  * Success Response
           Status - 200
           Content - {'Message': 'Movie Added Successfully'}

  * Error Response 
           Status - 400
           Content - {'error': 'The same movie is already created by another user. '}

           Status - 400
           Content - {'error': 'Movie already present..'}

$ http://localhost:8000/Movie/rating
  * Method -> POST
  * Url params
           Authorization: Token
           movie[String]
           rating[Number]

  * Success Response
           Status - 200
           Content - {'Message': 'Rated successfully!!!'}

  * Error Response 
           Status - 400
           Content - {'error': 'You've already rated this movie'}

           Status - 400
           Content - {'error': 'You can not rate your own movie'}

           Status - 400
           Content - {'error': 'Movie doesn't exist'}

           Status - 400
           Content - {'error': 'You can't provide rating greater than 5 or less than 1'}

```