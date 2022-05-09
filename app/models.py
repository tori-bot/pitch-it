
from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    #model to create new users
    __tablename__='users'

    identity=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.identity'))
    pass_secure=db.Column(db.String(255))
    bio=db.Column(db.String(255))
    profile_pic_url=db.Column(db.String())
    comments=db.relationship('Comment',backref='user' ,lazy="dynamic")
    pitches=db.relationship('Pitch',backref='user' ,lazy="dynamic")

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

class Comment(db.Model):
    __tablename__='comments'

    identity=db.Column(db.Integer,primary_key=True)
    pitch_id=db.Column(db.Integer)
    pitch_title=db.Column(db.String)
    pitch_comment=db.Column(db.String)
    posted=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('users.identity'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls,identity):
        comments=Comment.query.filter_by(pitch_id=identity).all()
        return comments

class Pitch:
    #class to define pitch objects
    __tablename__='pitches'

    identity=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255))
    image_url=db.Column(db.String)
    category=db.Column(db.String)
    author=db.Column(db.String(255))
    description=db.Column(db.String)
    published=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('users.identity'))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,category):
        pitches=Pitch.query.filter_by(category).all()
        return pitches