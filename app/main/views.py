from crypt import methods
from ..models import User,Comment,Pitch
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required
from . import main
from .forms import UpdateProfile,CommentForm,PitchForm
from .. import db,photos

@main.route('/')
def index():
    title='Pitch it...One minute could change your life.'
    return render_template('index.html',title=title)

@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template('/profile/profile.html',user=user)

# @main.route('pitch/new/<int:identity>',methods=['GET','POST'])
# @login_required
# def new_pitch(title):
#     title='New Pitch'
#     user=User.query.filter_by(username=uname).first()
#    )

#         if user is None:
#             abort(404) 
#     pitch_form=PitchForm()
#     if pitch_form.validate_on_submit():
#         pitch=Pitch.query.filter_by(title=title).first(
        
#         return redirect(url_for('main.index'))
#         flash('')

#         title=form.title.data
#         description=form.description.data
#         image=form.image_url.data

#         new_pitch=Pitch()



@main.route('/pitch/<int:identity')
def pitch(identity):
    pitch=Pitch.query.filter_by(identity=identity).first()
    title=f'{pitch.title} '
    image=f'{pitch.image_url} '
    content=f'{pitch.description} '


    if pitch is None:
        abort(404)

    return render_template('pitch.html',pitch=pitch,title=title,image=image,content=content)

@main.route('/user/<uname>/update',methods=['GET','POST'])
def update_profile(uname):
    user=User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)
    
    form=UpdateProfile()

    if form.validate_on_submit():
        user.bio=form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form=form)

@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def update_pic(uname):
    user= User.query.filter_by(username = uname).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_url = path
        db.session.commit()

    return redirect(url_for('main.profile',uname=uname))

# @main.route('/comment',methods=['GET','POST'])
# @login_required
# def new_comment(identify):

#comment form view
#single pitch view
#index view of all pitches with categories
#upvote and downvote and comment button on every pitch 

