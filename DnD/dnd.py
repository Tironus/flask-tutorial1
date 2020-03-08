import sys
from os.path import dirname
sys.path.append(dirname(__file__))

import dnd_db
from flask import Flask, render_template, url_for, request, flash
import dnd_extensions
import dnd_forms
import dnd_calc
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

@app.route('/edit_hero', methods=["GET", "POST"])
def edit_hero():
    hero_data = ""
    mdb = dnd_extensions.mongo_client.OSRIC
    form = dnd_forms.EditHeroForm()
    dnd_forms.update_hero_list(mdb, form)
    hero_dict = dict(form.hero_id.choices)
    if len(hero_dict) <= 0:
        flash("no hero data to edit...")
    else:
        hero = hero_dict[1]
        hero = dnd_db.find_name(mdb, hero)
        hero_data = dnd_db.display_id(mdb, ObjectId(hero['_id']))
        if request.method == "POST":
            if len(dict(form.hero_id.choices)) <= 0:
                flash("no hero available to delete...")
            else:
                hero = dnd_db.find_name(mdb, dict(form.hero_id.choices).get(int(form.hero_id.data)))
                hero_data = dnd_db.display_id(mdb, ObjectId(hero['_id']))
                dnd_forms.update_hero_list(mdb, form)
                if form.display_hero.data is True:
                    dnd_forms.update_hero_list(mdb, form)
                    hero = dnd_db.find_name(mdb, dict(form.hero_id.choices).get(int(form.hero_id.data)))
                    hero_data = dnd_db.display_id(mdb, ObjectId(hero['_id']))
                    dnd_forms.clear_edit_fields(form)
                    return render_template('edit_hero.html', form=form, hero_data=hero_data)
                else:
                    print(hero)
                    if form.submit.data is True:
                        if form.hero_name.data != "":
                            dnd_db.edit_hero(mdb, hero['name'], 'name', form.hero_name.data)
                            dnd_forms.update_hero_list(mdb, form)

                        if form.strength.data != "":
                            dnd_db.edit_hero(mdb, hero['name'], 'strength', form.strength.data)
                            to_hit_bonus, damage_bonus, encumbrance_bonus, str_minor_tests_bonus, str_major_tests_bonus = dnd_calc.calc_strength(form.strength.data)
                            dnd_db.edit_hero(mdb, hero['name'], 'str_to_hit', to_hit_bonus)
                            dnd_db.edit_hero(mdb, hero['name'], 'str_damage', damage_bonus)
                            dnd_db.edit_hero(mdb, hero['name'], 'str_encumbrance:', encumbrance_bonus)
                            dnd_db.edit_hero(mdb, hero['name'], 'str_min_test:', str_minor_tests_bonus)
                            dnd_db.edit_hero(mdb, hero['name'], 'str_maj_test:', str_major_tests_bonus)

                        if form.dexterity.data != "":
                            dnd_db.edit_hero(mdb, hero['name'], 'dexterity', form.dexterity.data)
                            surprise_bonus, missile_bonus_to_hit, ac_adjustment = dnd_calc.calc_dexterity(form.dexterity.data)
                            dnd_db.edit_hero(mdb, hero['name'], 'dxt_surprise', surprise_bonus)
                            dnd_db.edit_hero(mdb, hero['name'], 'dxt_missile_to_hit', missile_bonus_to_hit)
                            dnd_db.edit_hero(mdb, hero['name'], 'dxt_ac:', ac_adjustment)

                        if form.wisdom.data != "":
                            dnd_db.edit_hero(mdb, hero['name'], 'wisdom', form.wisdom.data)
                            mst = dnd_calc.calc_wisdom(form.wisdom.data)
                            dnd_db.edit_hero(mdb, hero['name'], 'wis_mental_save', mst)

                        if form.constitution.data != "":
                            dnd_db.edit_hero(mdb, hero['name'], 'constitution', form.constitution.data)
                            hpb, maj, min = dnd_calc.calc_constitution(form.constitution.data, hero['class'])
                            dnd_db.edit_hero(mdb, hero['name'], 'con_hp', hpb)
                            dnd_db.edit_hero(mdb, hero['name'], 'con_maj_test', maj)
                            dnd_db.edit_hero(mdb, hero['name'], 'con_min_test', min)

                        if form.intellect.data != "":
                            dnd_db.edit_hero(mdb, hero['name'], 'intellect', form.intellect.data)
                            al = dnd_calc.calc_intelligence(form.intellect.data)
                            print(al)
                            dnd_db.edit_hero(mdb, hero['name'], 'int_add_lang', al)

                        dnd_forms.update_hero_list(mdb, form)
                        hero = dnd_db.find_name(mdb, dict(form.hero_id.choices).get(int(form.hero_id.data)))
                        hero_data = dnd_db.display_id(mdb, ObjectId(hero['_id']))
                        dnd_forms.clear_edit_fields(form)
                        print(hero)
                        return render_template('edit_hero.html', form=form, hero_data=hero_data)
                    else:
                        dnd_forms.update_hero_list(mdb, form)
                        dnd_forms.clear_edit_fields(form)
                        return render_template('edit_hero.html', form=form, hero_data=hero_data)
    dnd_forms.update_hero_list(mdb, form)
    return render_template('edit_hero.html', form=form, hero_data=hero_data)

if __name__ == "__main__":
    app.run(debug=True)