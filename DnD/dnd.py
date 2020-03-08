import sys
from os.path import dirname
sys.path.append(dirname(__file__))

import dnd_db
from flask import Flask, render_template, url_for, request, flash
import dnd_extensions
import dnd_forms
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xb0B\x03f\x08\x84\xe8\xc7\xf2Y\x9e\x8bT\xcc\xd0\x03\xba\xb3f\x8a9\x95\xae\xa6'

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
        flash("search query sent...")
    return render_template('find_hero.html', heroes=heroes, form=form, hero_name=form.hero.data)

@app.route('/display_hero', methods=["GET", "POST"])
def display_hero():
    hero_data = ""
    mdb = dnd_extensions.mongo_client.OSRIC
    form = dnd_forms.DisplayHeroForm()
    dnd_forms.update_hero_list(mdb, form)
    if request.method == "POST":
        if len(dict(form.hero_id.choices)) <= 0:
            flash("no hero to display...")
        else:
            hero = dnd_db.find_name(mdb, dict(form.hero_id.choices).get(int(form.hero_id.data)))
            hero_data = dnd_db.display_id(mdb, ObjectId(hero['_id']))
            flash("hero query sent...")
    return render_template('display_hero.html', form=form, hero_data=hero_data)

@app.route('/create_hero', methods=["GET", "POST"])
def create_hero():
    form = dnd_forms.CreateHeroForm()
    if request.method == "POST":
        mdb = dnd_extensions.mongo_client.OSRIC
        ret = dnd_db.find_name(mdb, form.name.data)
        if ret is None:
            attribute_list = dnd_db.calculate_character(mdb, form)
            ret = dnd_db.create_doc(mdb, form.name.data, form, attribute_list)
            flash("hero id created...{}".format(ret.inserted_id))
        else:
            flash("hero id exists: {}".format(ret['_id']))
    return render_template('create_hero.html', form=form)

@app.route('/delete_hero', methods=["GET", "POST"])
def delete_hero():
    hero_data = ""
    mdb = dnd_extensions.mongo_client.OSRIC
    form = dnd_forms.DeleteHeroForm()
    dnd_forms.update_hero_list(mdb, form)
    if request.method == "POST":
        if len(dict(form.hero_id.choices)) <= 0:
            flash("no hero available to delete...")
        else:
            hero = dnd_db.find_name(mdb, dict(form.hero_id.choices).get(int(form.hero_id.data)))
            delete_result = dnd_db.delete_name(mdb, hero['name'])
            if delete_result.raw_result['n'] == 0:
                flash("hero delete FAILED...")
            elif delete_result.raw_result['n'] == 1:
                flash("hero delete SUCCESS...")
            dnd_forms.update_hero_list(mdb, form)
    return render_template('delete_hero.html', form=form, hero_data=hero_data)

if __name__ == "__main__":
    app.run(debug=True)