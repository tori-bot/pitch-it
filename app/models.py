from turtle import backward
from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    #model to create new users
    __tablename__='users'

    identity=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    role_id=db.Column(db.Integer,db.ForeignKey('roles.identity'))
    pass_secure=db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username} '

class Role(db.Model):
    #class to define different roles
    __tablename__='roles'

    identity=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
    users=db.relationship('User',backref='role' ,lazy="dynamic")


    def __repr__(self):
        return f'User {self.name} '

# class Comment(db.Model):
#     __tablename__='comment'

#     identity=db.Column(db.Integer,primary_key=True)
#     pitch_id=db.Column(db.Integer)
#     pitch_title=db.Column(db.String)
#     pitch_comment=db.Column(db.String)
#     posted=db.Column(db.DateTime,default=datetime.utcnow)