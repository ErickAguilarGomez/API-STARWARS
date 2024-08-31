from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    favoritos = db.relationship("Favoritos", backref="user", lazy=True)

    def __repr__(self):
        return "<User %r>" % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    favoritos = db.relationship("Favoritos", backref="character", lazy=True)

    def __repr__(self):
        return "<User %r>" % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "gender": self.gender,
        }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(10), nullable=False)
    terrain = db.Column(db.String(10), nullable=False)
    favoritos = db.relationship("Favoritos", backref="planet", lazy=True)

    def __repr__(self):
        return "<User %r>" % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(10), nullable=False)
    class_name = db.Column(db.String(10), nullable=False)
    favoritos = db.relationship("Favoritos", backref="vehicle", lazy=True)

    def __repr__(self):
        return "<User %r>" % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }


class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"), nullable=True)
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"), nullable=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.id"), nullable=True)

    def __repr__(self):
        return "<Favoritos %r>" % self.id

    def serialize(self):
        return {
            "id": self.id,
            "character": self.character.serialize() if self.character_id else None,
            "planet": self.planet.serialize() if self.planet_id else None,
            "vehicle": self.vehicle.serialize() if self.vehicle_id else None,
        }
