from email.mime import image
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired,Optional 

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment=TextAreaField('Leave a comment',validators=[InputRequired()])
    submit=SubmitField('Submit')


class PitchForm(FlaskForm):
    # image=
    category=SelectField('category',choices=[('pickup line','pickup line'),('business idea','business idea'),('tech startup','tech startup'),('art project','art project'),('vacation plan','vacation plan'),('marketing strategy','marketing strategy')],validators=[Optional()])
    title=StringField('pitch title',validators=[InputRequired()])
    author=StringField('author',validators=[InputRequired()])
    description=TextAreaField('description',validators=[InputRequired()])
    submit=SubmitField('Submit')
