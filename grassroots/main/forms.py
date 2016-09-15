from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(Form):
    """Accepts a nickname and a room."""
    name = StringField('Name', validators=[DataRequired()])
    loc = StringField('Location', validators=[DataRequired()])
    room = StringField('Service', validators=[DataRequired()])
    submit = SubmitField('Submit SOS')


class AdminForm(Form):
    """Accepts a nickname and a room."""
    name = StringField('Name', validators=[DataRequired()])
    room = StringField('Service', validators=[DataRequired()])
    submit = SubmitField('Monitor Requests')
