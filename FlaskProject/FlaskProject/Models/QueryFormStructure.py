from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class QueryFormStructure(object):
    """description of class"""
    name   = StringField('Country Name?)', validators = [DataRequierd()])
    submit = SubmitField('Submit')


