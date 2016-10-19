from sqlalchemy.ext.declarative import declarative_base
from muffin import db

__author__ = 'ife'


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
                            onupdate=db.func.current_timestamp())


    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception:
            pass
        return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception:
            pass
        return False

    def update_by_id(self):
        if self.id is None:
            return False
        else:
            db.session.commit(self)
            return True

    def select_by_id(self):
        if self.id is None:
            return None
        else:
            return self.query.filter(db.text('id = ' + str(self.id))).first()

