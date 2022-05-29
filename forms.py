from flask_wtf import FlaskForm
from wtforms import SubmitField , TextAreaField,FileField
from wtforms.validators import Length

class OriginalTextForm(FlaskForm):
    original_text = TextAreaField('Original text', 
                    validators = [Length(min=20, max=10000)],
                    render_kw = {'placeholder':'Enter Your News text ...'})
    
    generate = SubmitField('Random News')
    predict = SubmitField('Check News')
    
class OriginalImageForm(FlaskForm):
    original_text = FileField('Original image', 
                    render_kw = {'placeholder':'Enter Your News image ...'})
    
    predict = SubmitField('Check News')
