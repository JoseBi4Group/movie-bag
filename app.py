from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from database.db import initialize_db
from resources.movie import movies
from resources.user import users

app = Flask(__name__)
bcrypt = Bcrypt(app)

#app.config.from_envvar('ENV_FILE_LOCATION')
app.config['JWT_SECRET_KEY'] = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'

jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
}

initialize_db(app)
app.register_blueprint(users)
app.register_blueprint(movies)


app.run()