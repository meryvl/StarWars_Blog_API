"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User , People , Planet ,Favoritos
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)



# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code




# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def getUsers():
    try:
        users = User.query.all()
        toReturn = [users.serialize() for users in users]
        return jsonify(toReturn), 200

    except Exception:
        return jsonify({"msg": "Ha ocurrido un error"}) , 500
    
@app.route('/people', methods=['GET'])
def getpeoples():
    try:
        peoples = People.query.all()
        toReturnPeoples = [peoples.serialize() for peoples in peoples]
        return jsonify(toReturnPeoples), 200

    except Exception:
        return jsonify({"msg": "Ha ocurrido un error"}) , 500
    


@app.route('/people/<int:position>', methods=['GET'])
def getPeopleId(position):
    try:
       
        peopleId =  People.query.filter_by(People[position])
        
        return jsonify(people.serialize()), 200

    except Exception:
        return jsonify({"msg": "Ha ocurrido un error"}) , 500
    
       

@app.route('/Planet', methods=['GET'])
def getPlanets():
    try:
        planets = Planet.query.all()
        toReturnPlanets = [planets.serialize() for planets in planets]
        return jsonify(toReturnPlanets), 200

    except Exception:
        return jsonify({"msg": "Ha ocurrido un error"}) , 500
    
       








# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
