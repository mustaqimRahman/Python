from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import InputRequired

class  UrlShortener(FlaskForm):
    url = StringField('url', validators=[InputRequired()], render_kw={'style': 'width: 100ch'})
    submit = SubmitField('Generate URL')
