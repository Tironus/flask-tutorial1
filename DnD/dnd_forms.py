from flask_wtf import Form
from wtforms.fields import StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired
import dnd_db
import dnd_extensions

def update_hero_list(mdb, form):
    hero_list = dnd_db.find_all_names(mdb.dnd)
    if form.__name__() == 'DisplayHeroForm':
        form.hero_id.choices = hero_list
    elif form.__name__() == 'DeleteHeroForm':
        form.hero_id.choices = hero_list
    elif form.__name__() == 'EditHeroForm':
        form.hero_id.choices = hero_list

def clear_edit_fields(form):
    form.hero_name.data = ""
    form.strength.data = ""
    form.dexterity.data = ""
    form.wisdom.data = ""
    form.constitution.data = ""


class_choices = [('1', 'ranger'), ('2', 'cleric'), ('3', 'druid'), ('4', 'assassin'), ('5','fighter'), ('6','illusionist'), ('7','magic user'), ('8','paladin'), ('9','thief')]
align_choices = [('1','lawful good'), ('2','neutral good'), ('3','chaotic good'), ('4','lawful neutral'), ('5','neutral'), ('6', 'chaotic neutral'), ('7','lawful evil'), ('8','neutral evil'), ('9','chaotic evil')]
race_choices = [('1','dwarves'), ('2','elves'), ('3','gnomes'), ('4','half elves'), ('5','halflings'), ('6','half orcs'), ('7','humans')]
sex_choices = [('1','male'), ('2','female')]


class FindHeroForm(Form):
    hero = StringField('Hero Name:', validators=[DataRequired()])

class EditHeroForm(Form):
    def __name__(self):
        return "EditHeroForm"

    hero_id = SelectField('Hero:', choices=[])
    hero_name = StringField('Name:')
    strength = StringField('Strength:')
    dexterity = StringField('Dexterity:')
    wisdom = StringField('Wisdom:')
    constitution = StringField('Constitution:')
    display_hero = SubmitField('Get Hero Data')
    submit = SubmitField('Edit Hero')

class DeleteHeroForm(Form):
    def __name__(self):
        return "DeleteHeroForm"

    hero_id = SelectField('Hero:', choices=[])
    submit = SubmitField('Delete Hero')

class DisplayHeroForm(Form):
    def __name__(self):
        return "DisplayHeroForm"

    hero_id = SelectField('Hero:', choices=[])
    submit = SubmitField('Display Hero')

class CreateHeroForm(Form):
    name = StringField('Hero Name:', validators=[DataRequired()])
    cclass = SelectField('Class:', choices=class_choices)
    align = SelectField('Alignment:', choices=align_choices)
    race = SelectField('Race:', choices=race_choices)
    str = StringField('Strength:', validators=[DataRequired()])
    dxt = IntegerField('Dexterity:', validators=[DataRequired()])
    wis = IntegerField('Wisdon:', validators=[DataRequired()])
    int = IntegerField('Intellect:', validators=[DataRequired()])
    cha = IntegerField('Charisma:', validators=[DataRequired()])
    con = IntegerField('Constitution:', validators=[DataRequired()])
    xp = IntegerField('XP:', validators=[DataRequired()])
    hp = IntegerField('HP:', validators=[DataRequired()])
    ac = IntegerField('AC:', validators=[DataRequired()])
    age = IntegerField('Age:', validators=[DataRequired()])
    height = StringField('Height:', validators=[DataRequired()])
    weight = StringField('Weight:', validators=[DataRequired()])
    sex = SelectField('Sex:', choices=sex_choices)
    submit = SubmitField('Save Hero')