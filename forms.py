from flask_wtf import FlaskForm
from wtforms import SubmitField , TextAreaField
from wtforms.validators import Length

class OriginalTextForm(FlaskForm):
    original_text = TextAreaField('Original text', 
                    validators = [Length(min=20, max=10000)],
                    render_kw = {'placeholder':'Enter Your News ...'})
    
    generate = SubmitField('Random News')
    predict = SubmitField('Check News')

