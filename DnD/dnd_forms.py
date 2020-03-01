from flask_wtf import Form
from wtforms.fields import StringField
from wtforms.validators import DataRequired

class FindHeroForm(Form):
    hero = StringField('Hero Name:', validators=[DataRequired()])