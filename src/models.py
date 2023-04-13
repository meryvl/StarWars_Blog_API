from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.email
    

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Favoritos(db.Model):
    __tablename__ = 'favoritos'
   
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    usuario = db.relationship(User)
  


    def __repr__(self):
        return '<Favoritos %r>' % self.favoritosname
    

    def serialize(self):
        return {
            "id": self.id,
            "usuario id": self.usuario_id,
            "usuario" : self.usuario
        }



class Planet(db.Model):
    __tablename__ = 'planet'
  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),nullable=False)
    descripcion = db.Column(db.String(250))
    population = db.Column(db.String(250))
    Diameter = db.Column(db.String(250))
    atmósfera = db.Column(db.String(250))
    
    def __repr__(self):
        return '<Planet %r>' % self.plnatname
    

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.descripcion,
            "population": self.population,
            "dimension" : self.Diameter,
            "atmosfera" : self.atmosfera,
    
        }


class Vehicles(db.Model): 
     __tablename__ = 'vehicles'
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(250),nullable=False)
     Model = db.Column(db.String(250))
     cargo_capacity= db.Column(db.String(250))
     consumables= db.Column(db.String(250))
     favorito_id = db.Column(db.Integer, db.ForeignKey('favoritos.id'))
     favoritos = db.relationship(Favoritos)
     
     
     def __repr__(self):
        return '<Vehicles %r>' % self.planetname

     def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "Model": self.Model,
            "capacity": self.cargo_capacity,
            "comsumable" : self.consumables,
            "favorito id" : self.favorito_id,
            "favorito" : self.favoritos
    
        }


class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    descripcion = db.Column(db.String(250))
    height = db.Column(db.String(250))
    year= db.Column(db.String(250))
   
    

    def __repr__(self):
        return '<People %r>' % self.peoplename

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "descripcion ": self.descripcion ,
            "height": self.height,
            "year" : self.year,
            
           
        }




    
    
    
    
    