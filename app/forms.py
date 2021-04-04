from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired

class EntryForm(FlaskForm):
    entry = StringField('Entry',validators=[DataRequired()])
    project = StringField('Project')
    notes = StringField('Notes') 
    save = SubmitField('Save')