from flask_wtf import Form
from wtforms.fields import StringField
from wtforms.validators import DataRequired

class FindHeroForm(Form):
    hero = StringField('Hero Name:', validators=[DataRequired()])

class DisplayHeroForm(Form):
    hero_id = StringField('Hero ID:', validators=[DataRequired()])

class CreateHeroForm(Form):
    name = StringField('Hero Name:', validators=[DataRequired()])
    attr1 = StringField('Attribute 1:', validators=[DataRequired()])
    attr2 = StringField('Attribute 2:', validators=[DataRequired()])
    attr3 = StringField('Attribute 3:', validators=[DataRequired()])