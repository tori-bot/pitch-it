
from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user
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
    pass_secure=db.Column(db.String(255))
    bio=db.Column(db.String(255))
    profile_pic_url=db.Column(db.String())
    comments=db.relationship('Comment',backref='user' ,lazy="dynamic")
    pitches=db.relationship('Pitch',backref='user' ,lazy="dynamic")
    upvotes = db.relationship('Upvote', backref = 'user', lazy = 'dynamic')
    downvotes = db.relationship('Downvote', backref = 'user', lazy = 'dynamic')

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

class Pitch(db.Model):
    #class to define pitch objects
    __tablename__='pitches'

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255))
    category=db.Column(db.String)
    author=db.Column(db.String(255))
    content=db.Column(db.Text)
    published=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    comments=db.relationship('Comment',backref='pitch',lazy="dynamic")
    upvotes = db.relationship('Upvote', backref = 'pitch', lazy = 'dynamic')
    downvotes = db.relationship('Downvote', backref = 'pitch', lazy = 'dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,category):
        pitches=Pitch.query.filter_by(category=category).all()
        return pitches

    def __repr__(self):
        return(f"User ('{self.title}','{self.published}')")

class Comment(db.Model):
    __tablename__='comments'

    id=db.Column(db.Integer,primary_key=True)
    pitch_id_comment=db.Column(db.Integer,db.ForeignKey('pitches.id',ondelete='CASCADE'))
    content=db.Column(db.Text)
    posted=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def add_comment(cls,id):
        comment = Comment(user = current_user, pitch_id=id)
        comment.save_comment()

    @classmethod
    def get_comment(cls,id):
        comments=Comment.query.filter_by(pitch_id=id).all()
        return comments

    def __repr__(self):
        return(f"User('{self.content}', '{self.posted}')")

class Upvote(db.Model):
    
  __tablename__ = 'upvotes'

  id = db.Column(db.Integer, primary_key=True)
  upvote = db.Column(db.Integer, default = 0)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  pitch_id_upvote = db.Column(db.Integer, db.ForeignKey('pitches.id'))

  def save_upvotes(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def add_upvotes(cls,id):
    upvote_pitch = Upvote(user = current_user, pitch_id_upvote=id)
    upvote_pitch.save_upvotes()

    
  @classmethod
  def get_upvotes(cls,id):
    upvote = Upvote.query.filter_by(pitch_id_upvote=id).all()
    return upvote

  @classmethod
  def get_all_upvotes(cls,pitch_id):
    upvotes = Upvote.query.order_by('id').all()
    return upvotes

  def __repr__(self):
    return f'{self.user_id}:{self.pitch_id}'

class Downvote(db.Model):
    
  __tablename__ = 'downvotes'

  id = db.Column(db.Integer, primary_key=True)
  downvote = db.Column(db.Integer, default=0)
  pitch_id_downvote = db.Column(db.Integer, db.ForeignKey('pitches.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def save_downvotes(self):
    db.session.add(self)
    db.session.commit()


  def add_downvotes(cls, id):
      downvote_pitch = Downvote(user = current_user, pitch_id=id)
      downvote_pitch.save_downvotes()

  
  @classmethod
  def get_downvotes(cls, id):
    downvote = Downvote.query.filter_by(pitch_id=id).all()
    return downvote

  @classmethod
  def get_all_downvotes(cls, pitch_id):
    downvote = Downvote.query.order_by('id').all()
    return downvote

  def __repr__(self):
    return f'{self.user_id}:{self.pitch_id}'

