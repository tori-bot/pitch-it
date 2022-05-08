from . import db

class User(db.Model):
    #model to create new users
    __tablename__='users'

    identity=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    role_id=db.Column(db.Integer,db.ForeignKey('roles.identity'))

    def __repr__(self):
        return f'User {self.username} '

class Role(db.Model):
    #class to define different roles
    __tablename__='roles'

    identity=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.name} '