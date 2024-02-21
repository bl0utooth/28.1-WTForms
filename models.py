from flask_sqlalchemy import SQLAlchemy 

base_image_url = 'https://www.ketk.com/wp-content/uploads/sites/34/2020/08/clear-the-shelters-generic.jpg?w=900'

db = SQLAlchemy()

class Pet(db.model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        return self.photo_url or base_image_url


def connect_db(app):
    db.app = app
    db.init_app(app)