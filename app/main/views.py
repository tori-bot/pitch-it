from crypt import methods
from unicodedata import category
from ..models import User,Comment,Pitch
from flask import render_template,request,redirect,url_for,abort
from flask_login import current_user, login_required
from . import main
from .forms import UpdateProfile,CommentForm,PitchForm
from .. import db,photos
import markdown2

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

@main.route('pitch/new/<int:identity>',methods=['GET','POST'])
@login_required
def new_pitch(uname):
    title='New Pitch'
    user=User.query.filter_by(username=uname).first()

    if user is None:
        abort(404) 

    pitch_form=PitchForm()
    if pitch_form.validate_on_submit():
        title=pitch_form.title.data
        category=pitch_form.category.data
        author=pitch_form.author.data
        description=pitch_form.description.data

        new_pitch=Pitch(title=title,category=category, author=author, content=description)

        new_pitch.save_pitch()
        
        return redirect(url_for('main.index'))
    else:
        pitches=Pitch.query.order_by(Pitch.published).all
        

    return render_template('new_pitch.html',title=title,pitch_form=pitch_form,pitches=pitches)



@main.route('/pitch/<int:identity>')
def pitch(id):
    pitch=Pitch.query.get(id)
    title=f'{pitch.title} '
    category=f'{pitch.category} '
    author=f'{pitch.author} '
    description=f'{pitch.description} '


    if pitch is None:
        abort(404)

    return render_template('pitch.html',pitch=pitch,title=title,category=category,author=author,description=description)

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

@main.route('/comment/<int:pitch_id>',methods=['GET','POST'])
@login_required
def new_comment(pitch_id):
    comment_form=CommentForm()
    pitch=Pitch.query.get(pitch_id)
    comments=Comment.query.filter_by(pitch_id=pitch_id).all()

    if comment_form.validate_on_submit():
        content=comment_form.content.data
        user_id=current_user._get_current_object().id

        new_comment=Comment(content=content,user_id=user_id,pitch_id=pitch_id)

        new_comment.save_comment()

        return redirect(url_for('main.new_comment',pitch_id=pitch_id))
    
    return render_template('new_comment.html',pitch=pitch,comments=comments,comment_form=comment_form)

@main.route('/pitch/comment/<int:pitch_id>')
@login_required
def comment(id):
    comment=Pitch.query.get(id)
    if comment is None:
        abort(404)
    
    format_comment = markdown2.markdown(comment.content,extras=["code-friendly","fenced-code blocks"])
    return render_template('comment.html',comment=comment,format_comment=format_comment)
        

#comment form view
#single pitch view
#index view of all pitches with categories
#upvote and downvote and comment button on every pitch 

