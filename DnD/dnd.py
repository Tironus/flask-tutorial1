import dnd_db
from flask import Flask, render_template, url_for, request
import dnd_extensions
import dnd_forms
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

@app.route('/')
@app.route('/index')
def dnd():
    return render_template('index.html')

@app.route('/find_hero', methods=["GET", "POST"])
def find_hero():
    heroes = []
    form = dnd_forms.FindHeroForm()
    if request.method == "POST":
        mdb = dnd_extensions.mongo_client.OSRIC
        heroes = dnd_db.display_name(mdb, form.hero.data)
    return render_template('find_hero.html', heroes=heroes, form=form, hero_name=form.hero.data)

@app.route('/display_hero', methods=["GET", "POST"])
def display_hero():
    hero_data = ""
    form = dnd_forms.DisplayHeroForm()
    if request.method == "POST":
        mdb = dnd_extensions.mongo_client.OSRIC
        hero_data = dnd_db.display_id(mdb, ObjectId(form.hero_id.data))
    return render_template('display_hero.html', form=form, hero_data=hero_data)

if __name__ == "__main__":
    app.run(debug=True)