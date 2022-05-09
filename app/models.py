
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

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255),unique=True)
    email = db.Column(db.String(255),unique = True,index = True)
    # role_id=db.Column(db.Integer,db.ForeignKey('roles.role_id'))
    pass_secure=db.Column(db.String(255))
    bio=db.Column(db.String(255))
    profile_pic_url=db.Column(db.String())
    comments=db.relationship('Comment',backref='author' ,lazy="dynamic")
    pitches=db.relationship('Pitch',backref='author' ,lazy="dynamic")

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

# class Role(db.Model):
#     #class to define different roles
#     __tablename__='roles'

#     role_id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(255))
#     users=db.relationship('User',backref='role' ,lazy="dynamic")


    # def __repr__(self):
    #     return f'User {self.name} '

class Comment(db.Model):
    __tablename__='comments'

    id=db.Column(db.Integer,primary_key=True)
    pitch_id=db.Column(db.Integer,db.ForeignKey('pitches.id',ondelete='CASCADE'))
    content=db.Column(db.Text)
    posted=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))

    # def save_comment(self):
    #     db.session.add(self)
    #     db.session.commit()

    # @classmethod
    # def get_comment(cls,identity):
    #     comments=Comment.query.filter_by(pitch_id=identity).all()
    #     return comments
    def __repr__(self):
        return(f"User('{self.content}', '{self.posted}')")
class Pitch:
    #class to define pitch objects
    __tablename__='pitches'

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255))
    image_url=db.Column(db.String)
    category=db.Column(db.String)
    author=db.Column(db.String(255))
    content=db.Column(db.Text)
    published=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('users.user_id'))
    comments=db.relationship('Comment',backref='pitch',lazy="dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,category):
        pitches=Pitch.query.filter_by(category=category).all()
        return pitches

    def __repr__(self):
        return(f"User ('{self.title}','{self.published}')")

