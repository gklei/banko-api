from db import db

class LinkItemModel(db.Model):
  __tablename__ = 'linkitems'

  id = db.Column(db.Integer, primary_key=True)
  item_id = db.Column(db.String(80))
  access_token = db.Column(db.String(80))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def __init__(self, item_id: str, access_token: str, user_id: int):
    self.item_id = item_id
    self.access_token = access_token
    self.user_id = user_id

  def json(self):
    return {'item_id': self.item_id}

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def delete_from_db(self):
      db.session.delete(self)
      db.session.commit()
  
  @classmethod
  def find_by_user_id(cls, user_id):
    return cls.query.filter_by(user_id=user_id).all()
  
  @classmethod
  def find_by_item_id(cls, item_id):
    return cls.query.filter_by(item_id=item_id).first()