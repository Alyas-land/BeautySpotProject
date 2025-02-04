import datetime
from config import db
from werkzeug.security import generate_password_hash
from persiantools.jdatetime import JalaliDateTime
import pytz

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    created_at = db.Column(db.String(20), default=JalaliDateTime.now().strftime("%Y/%m/%d - %H:%M"), nullable=False)
    last_login = db.Column(db.String(20), nullable=False)


    # relation to reservation model
    reservation = db.relationship('Reservation', back_populates='user')


    def __init__(self, name: str, username: str, password: str, phone_number: str):
        self.name = name
        self.username = username
        self.password = generate_password_hash(password)
        self.phone_number = phone_number
        self.created_at = JalaliDateTime.strftime('%Y/%m/%d - %H:%M')


    def last_login_update(self):
        self.last_login = JalaliDateTime.now().strftime("%Y/%m/%d - %H:%M")

    


class Reservation(db.Model):
    __tablename__ = 'reservation'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    service_type = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.String(20), default=JalaliDateTime.now().strftime("%Y/%m/%d - %H:%M"), nullable=False)
    reserve_time = db.Column(db.DateTime, nullable=False)

    # relation to reservation user
    user = db.relationship('User', back_populates='reservations')

    def __init__(self, title: str, description: str, service_type: str, reserve_time: str):
        self.title = title
        self.description = description
        self.service_type = service_type
        self.reserve_time = reserve_time













