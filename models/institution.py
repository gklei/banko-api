from db import db

class Institution(db.Model):
  __tablename__ = 'institutions'

  id = db.Column(db.Integer, primary_key=True)
  