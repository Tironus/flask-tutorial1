from bson.objectid import ObjectId
import dnd_calc

def create_doc(mongo_db, name, form, attributes):
    character = {
        'name' : name,
        'strength' : attributes[0],
        'dexterity' : attributes[1],
        'wisdom' : attributes[2],
        'intellect' : attributes[3],
        'charisma' : attributes[4],
        'constitution' : attributes[5],
        'class': dict(form.cclass.choices).get(form.cclass.data),
        'alignment': dict(form.align.choices).get(form.align.data),
        'race': dict(form.race.choices).get(form.race.data),
        'xp': form.xp.data,
        'hp:': form.hp.data,
        'ac': form.ac.data,
        'age': form.age.data,
        'height': form.height.data,
        'weight': form.weight.data,
        'sex': dict(form.sex.choices).get(form.sex.data),
        'str_to_hit': attributes[6],
        'str_damage': attributes[7],
        'str_encumbrance': attributes[8],
        'str_min_test': attributes[9],
        'str_maj_test': attributes[10],
        'dxt_surprise': attributes[11],
        'dxt_missile_to_hit': attributes[12],
        'dxt_ac': attributes[13],
        'con_hp': attributes[14],
        'con_min_test': attributes[15],
        'con_maj_test': attributes[16],
        'wis_mental_save': attributes[17],
        'int_add_lang': attributes[18],
        'cha_max_henchman': attributes[19],
        'cha_loyalty': attributes[20],
        'cha_reaction' : attributes[21]
    }

    result = mongo_db.dnd.insert_one(character)
    return result

def display_name(mongo_db, name):
    result_list = []
    result = mongo_db.dnd.find({'name' : name})
    for doc in result:
        result_list.append(doc)
    return result_list

def display_id(mongo_db, id):
    result = mongo_db.dnd.find({'_id' : ObjectId(id)})
    for doc in result:
        return doc

def find_name(mongo_db, name):
    query = {"name": name}
    result = mongo_db.dnd.find_one(query)
    return result

def delete_name(mongo_db, name):
    query = {"name": name}
    result = mongo_db.dnd.delete_one(query)
    return result

def find_all_names(col):
    hero_list = []
    counter = 1
    for hero in col.find():
        hero_list.append((counter, str(hero['name'])))
        counter += 1
    return hero_list

def edit_hero(mongo_db, name, attribute, new_value):
    query = {'name': name}
    attr = {attribute: new_value}
    result = mongo_db.dnd.find_one_and_update(query, {'$set': attr})
    return result

def calculate_character(mongo_db, form_data):
    attributes_list = []

    # Strength Scores
    to_hit_bonus = 0
    damage_bonus = 0
    encumbrance_bonus = 0
    str_minor_tests_bonus = 0
    str_major_tests_bonus = 0
    strength_score = form_data.str.data
    to_hit_bonus, damage_bonus, encumbrance_bonus, str_minor_tests_bonus, str_major_tests_bonus = dnd_calc.calc_strength(strength_score)

    # Dexterity Scores
    surprise_bonus = 0
    missile_bonus_to_hit = 0
    ac_adjustment = 0
    dexterity_score = form_data.dxt.data
    surprise_bonus, missile_bonus_to_hit, ac_adjustment = dnd_calc.calc_dexterity(dexterity_score)

    # Constitution Scores
    hp_bonus = 0
    con_maj_test = 0
    con_min_test = 0
    constitution_score = form_data.con.data
    hp_bonus, con_maj_test, con_min_test = dnd_calc.calc_constitution(constitution_score, form_data.cclass.data)

    # Intelligence Scores
    additional_lang = 0
    intelligence_score = form_data.int.data
    additional_lang = dnd_calc.calc_intelligence(intelligence_score)

    # Wisdom Scores
    saving_throw_bonus = 0
    wisdom_score = form_data.wis.data
    saving_throw_bonus = dnd_calc.calc_wisdom(wisdom_score)

    # Charisma Scores
    max_henchman = 0
    loyalty_bonus = 0
    reaction_bonus = 0
    charisma_score = form_data.cha.data
    max_henchman, loyalty_bonus, reaction_bonus = dnd_calc.calc_charisma(charisma_score)

    # Generate attributes list
    # primary attribute scores
    attributes_list.append(strength_score)
    attributes_list.append(dexterity_score)
    attributes_list.append(wisdom_score)
    attributes_list.append(intelligence_score)
    attributes_list.append(charisma_score)
    attributes_list.append(constitution_score)

    # strength attribute bonuses
    attributes_list.append(to_hit_bonus)
    attributes_list.append(damage_bonus)
    attributes_list.append(encumbrance_bonus)
    attributes_list.append(str_minor_tests_bonus)
    attributes_list.append(str_major_tests_bonus)

    # intellect attribute bonuses
    attributes_list.append(surprise_bonus)
    attributes_list.append(missile_bonus_to_hit)
    attributes_list.append(ac_adjustment)

    # constitution attribute bonuses
    attributes_list.append(hp_bonus)
    attributes_list.append(con_min_test)
    attributes_list.append(con_maj_test)

    # wisdom attribute bonuses
    attributes_list.append(saving_throw_bonus)
    attributes_list.append(additional_lang)

    # charisma attribute bonuses
    attributes_list.append(max_henchman)
    attributes_list.append(loyalty_bonus)
    attributes_list.append(reaction_bonus)

    return attributes_list