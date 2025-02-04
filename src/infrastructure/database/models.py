from config import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.Date, nullable=False)
    last_login = db.Column(db.Date, nullable=False)


    def __init__(self, name: str, username: str, password: str):
        self.name = name
        self.username = username
        self.password = generate_password_hash(password)

    


class Reserve(db.Model):
    pass











