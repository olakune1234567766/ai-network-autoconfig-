from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    sim_number = db.Column(db.String(50), unique=True, nullable=False)
    face_encoding = db.Column(db.Text, nullable=False)  # Stores face encoding as JSON
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)
    verification_count = db.Column(db.Integer, default=0)
    last_verification = db.Column(db.DateTime)
    
    def __repr__(self):
        return f'<User {self.name}>'

class VerificationLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False)  # success/failed
    confidence = db.Column(db.Float)
    ip_address = db.Column(db.String(50))
    
    user = db.relationship('User', backref=db.backref('verifications', lazy=True))