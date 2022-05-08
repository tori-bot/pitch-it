from . import db

class User(db.Model):
    #model to create new users
    __tablename__='users'

    identity=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username} '
