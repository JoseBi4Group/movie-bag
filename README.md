# movie-bag

This project is created to test Python + Flask + MongoDB following the next tutorial [Flask Rest API - Zero to Yoda](https://dev.to/paurakhsharma/flask-rest-api-part-0-setup-basic-crud-api-4650), but using structure of Blueprints insted of Flask-restful. MongoDB is managed by mongoengine.

## Python extensions installed

This application has the following extensions:
- Flask: `pipenv install flask`
- MongoEngine: `pipenv install flask-mongoengine`
- Encrypt passwords (bcrypt): `pipenv install flask-bcrypt`
- JWT for authentication: `pipenv instll flask-jwt-extended` 

## Run application

```
pipenv shell
python app.py
```
## Test application

### Users module

1. Add a new user.  
**URL:** `http://localhost:5000/users`   
**Method:** POST  
![add_users_postman](https://i.ibb.co/tXShGm1/add-users.png)  

2. Sign in with the user created.  
**URL:** `http://localhost:5000/users/login`  
**Method:** POST  
![sign_in_postman](https://i.ibb.co/XxFkmDG/sign-in.png)  

3. Get a list of users.  
**URL:** `http://localhost:5000/users`  
**Method:** GET  
![get_users_postman](https://i.ibb.co/9r0Xmb0/get-users.png)  

### Movies module

1. Add a new movie.  
**URL:** `http://localhost:5000/movies`  
**Method:** POST  
**Authorization:** Bearer Token (add user Token).  
![add_movie_postman](https://i.ibb.co/p38gJnM/add-movie.png)  

2. Get a list of movies.  
**URL:** `http://localhost:5000/movies`  
**Method:** GET  
**Authorization:** Bearer Token (add user Token).  
![movies_postman](https://i.ibb.co/847Lmz0/movies.png)  

3. Get a single movie.  
**URL:** `http://localhost:5000/movies/<id>`  
**Method:** GET  
**Authorization:** Bearer Token (add user Token).  
**url_params:** `_id`  
![movie_postman](https://i.ibb.co/cQvR2vx/get-movie.png)  

4. Update a movie.  
**URL:** `http://localhost:5000/movies/<id>`  
**Method:** PUT  
**Authorization:** Bearer Token (add user Token).  
**url_params:** `_id`  
![update_movie_postman](https://i.ibb.co/gyFFfRG/update-movie.png)  

5. Delete a movie.  
**URL:** `http://localhost:5000/movies/<id>`  
**Method:** DELETE  
**Authorization:** Bearer Token (add user Token).  
**url_params:** `_id`  
![delete_movie_postman](https://i.ibb.co/tYGvC2P/delete-movie.png)  
