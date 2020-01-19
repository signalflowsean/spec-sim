# ---- THIRD PARTY IMPORTS ----
from datetime import datetime

# ---- FIRST PART IMPORTS ---- 
from api import db

class User(db.Model): 
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  views = db.relationship('View', backref='author', lazy='dynamic')

  def __repr__(self): 
    return '<User {}>'.format(self.username)

class View(db.Model): 
  id = db.Column(db.Integer, primary_key=True)
  date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  status = db.Column(db.String(64))
  file_name = db.Column(db.String(64))
  file_path = db.Column(db.String(64))
  mfcc_raw = db.Column(db.String(120))
  mfcc_std_dev = db.Column(db.String(120))
  mfcc_mean =  db.Column(db.String(120))
  mfcc_avg_diff =  db.Column(db.String(120))
  mfcc_fixed =  db.Column(db.String(120))
  x_corr =  db.Column(db.String(120))
  y_corr = db.Column(db.String(120))

  def __repr__(self): 
    return '<View {}>'.format(self.status)
