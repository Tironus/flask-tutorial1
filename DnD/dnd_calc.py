def calc_strength(strength_score):
    to_hit_bonus = 0
    damage_bonus = 0
    encumbrance_bonus = 0
    str_minor_tests_bonus = 0
    str_major_tests_bonus = 0
    strength_score = int(strength_score)

    if strength_score == 3:
        to_hit_bonus += -3
        damage_bonus += -1
        encumbrance_bonus += -35
        str_minor_tests_bonus += 1
        str_major_tests_bonus += 0
    elif strength_score >= 4 and strength_score <= 5:
        to_hit_bonus += -2
        damage_bonus += -1
        encumbrance_bonus += -25
        str_minor_tests_bonus += 1
        str_major_tests_bonus += 0
    elif strength_score >= 6 and strength_score <= 7:
        to_hit_bonus += -1
        damage_bonus += 0
        encumbrance_bonus += -15
        str_minor_tests_bonus += 1
        str_major_tests_bonus += 0
    elif strength_score >= 8 and strength_score <= 9:
        to_hit_bonus += 0
        damage_bonus += 0
        encumbrance_bonus += 0
        str_minor_tests_bonus += 2
        str_major_tests_bonus += 1
    elif strength_score >= 10 and strength_score <= 11:
        to_hit_bonus += 0
        damage_bonus += 0
        encumbrance_bonus += 0
        str_minor_tests_bonus += 2
        str_major_tests_bonus += 2
    elif strength_score >= 12 and strength_score <= 13:
        to_hit_bonus += 0
        damage_bonus += 0
        encumbrance_bonus += 10
        str_minor_tests_bonus += 2
        str_major_tests_bonus += 4
    elif strength_score >= 14 and strength_score <= 15:
        to_hit_bonus += 0
        damage_bonus += 0
        encumbrance_bonus += 20
        str_minor_tests_bonus += 2
        str_major_tests_bonus += 7
    elif strength_score == 16:
        to_hit_bonus += 0
        damage_bonus += 1
        encumbrance_bonus += 35
        str_minor_tests_bonus += 3
        str_major_tests_bonus += 10
    elif strength_score == 17:
        to_hit_bonus += 1
        damage_bonus += 1
        encumbrance_bonus += 50
        str_minor_tests_bonus += 3
        str_major_tests_bonus += 13
    elif strength_score == 18:
        to_hit_bonus += 1
        damage_bonus += 2
        encumbrance_bonus += 75
        str_minor_tests_bonus += 3
        str_major_tests_bonus += 16
    elif strength_score >= 18.01 and strength_score <= 18.5:
        to_hit_bonus += 1
        damage_bonus += 3
        encumbrance_bonus += 100
        str_minor_tests_bonus += 3
        str_major_tests_bonus += 20
    elif strength_score >= 18.51 and strength_score <= 18.75:
        to_hit_bonus += 2
        damage_bonus += 3
        encumbrance_bonus += 125
        str_minor_tests_bonus += 4
        str_major_tests_bonus += 25
    elif strength_score >= 18.76 and strength_score <= 18.9:
        to_hit_bonus += 2
        damage_bonus += 4
        encumbrance_bonus += 150
        str_minor_tests_bonus += 4
        str_major_tests_bonus += 30
    elif strength_score >= 18.91 and strength_score <= 18.99:
        to_hit_bonus += 2
        damage_bonus += 5
        encumbrance_bonus += 200
        str_minor_tests_bonus += 6
        str_major_tests_bonus += 35
    elif strength_score == 19:
        to_hit_bonus += 3
        damage_bonus += 6
        encumbrance_bonus += 300
        str_minor_tests_bonus += 6
        str_major_tests_bonus += 40
    return to_hit_bonus, damage_bonus, encumbrance_bonus, str_minor_tests_bonus, str_major_tests_bonus

def calc_dexterity(dex_score):
    surprise_bonus = 0
    missile_bonus_to_hit = 0
    ac_adjustment = 0
    if dex_score == 3:
        surprise_bonus += -3
        missile_bonus_to_hit += -3
        ac_adjustment += 4
    elif dex_score == 4:
        surprise_bonus += -2
        missile_bonus_to_hit += -2
        ac_adjustment += 3
    elif dex_score == 5:
        surprise_bonus += -1
        missile_bonus_to_hit += -1
        ac_adjustment += 2
    elif dex_score == 6:
        surprise_bonus += 0
        missile_bonus_to_hit += 0
        ac_adjustment += 1
    elif dex_score >= 7 and dex_score <= 14:
        surprise_bonus += 0
        missile_bonus_to_hit += 0
        ac_adjustment += 0
    elif dex_score == 15:
        surprise_bonus += 0
        missile_bonus_to_hit += 0
        ac_adjustment += -1
    elif dex_score == 16:
        surprise_bonus += 1
        missile_bonus_to_hit += 1
        ac_adjustment += -2
    elif dex_score == 17:
        surprise_bonus += 2
        missile_bonus_to_hit += 2
        ac_adjustment += -3
    elif dex_score == 18 or dex_score == 19:
        surprise_bonus += 3
        missile_bonus_to_hit += 3
        ac_adjustment += -4
    return surprise_bonus, missile_bonus_to_hit, ac_adjustment

def calc_constitution(con_score, cclass):
    hpb = 0
    maj = 0
    min = 0
    bonus_list = ['fighter', 'paladin', 'ranger']
    if con_score == 3:
        hpb += -2
        maj += 40
        min += 35
    elif con_score == 4:
        hpb += -1
        maj += 45
        min += 40
    elif con_score == 5:
        hpb += -1
        maj += 50
        min += 45
    elif con_score == 6:
        hpb += -1
        maj += 55
        min += 50
    elif con_score == 7:
        hpb += 0
        maj += 60
        min += 55
    elif con_score == 8:
        hpb += 0
        maj += 65
        min += 60
    elif con_score == 9:
        hpb += 0
        maj += 70
        min += 65
    elif con_score == 10:
        hpb += 0
        maj += 75
        min += 70
    elif con_score ==11:
        hpb += 0
        maj += 80
        min += 75
    elif con_score == 12:
        hpb += 0
        maj += 85
        min += 80
    elif con_score == 13:
        hpb += 0
        maj += 90
        min += 85
    elif con_score == 14:
        hpb += 0
        maj += 92
        min += 88
    elif con_score == 15:
        hpb += 1
        maj += 94
        min += 91
    elif con_score == 16:
        hpb += 2
        maj += 96
        min += 95
    elif con_score == 17:
        hpb += 2
        maj += 98
        min += 97
        if cclass in bonus_list:
            hpb += 1
    elif con_score == 18:
        hpb += 2
        maj += 100
        min += 99
        if cclass in bonus_list:
            hpb += 2
    elif con_score == 19:
        hpb += 2
        maj += 100
        min += 99
        if cclass in bonus_list:
            hpb += 3
    return hpb, maj, min

def calc_intelligence(int_score):
    al = 0
    if int_score >= 8 or int_score <= 9:
        al += 1
    elif int_score >= 10 or int_score <= 11:
        al += 2
    elif int_score >= 12 or int_score <= 13:
        al += 3
    elif int_score >= 14 or int_score <= 15:
        al += 4
    elif int_score == 16:
        al += 5
    elif int_score == 17:
        al += 6
    elif int_score == 18:
        al += 7
    elif int_score == 19:
        al += 8
    return al

def calc_charisma(c_score):
    mh = 0
    loy = 0
    rea = 0
    if c_score == 3:
        mh += 1
        loy += -30
        rea += -25
    elif c_score == 4:
        mh += 1
        loy += -25
        rea += -20
    elif c_score == 5:
        mh += 2
        loy += -20
        rea += -15
    elif c_score == 6:
        mh += 2
        loy += -15
        rea += -10
    elif c_score == 7:
        mh += 3
        loy += -10
        rea += -5
    elif c_score == 8:
        mh += 3
        loy += -5
    elif c_score >= 9 and c_score <= 11:
        mh += 4
    elif c_score == 12:
        mh += 5
    elif c_score == 13:
        mh += 5
        rea += 5
    elif c_score == 14:
        mh += 6
        loy += 5
        rea += 10
    elif c_score == 15:
        mh += 7
        loy += 15
        rea += 15
    elif c_score == 16:
        mh += 8
        loy += 20
        rea += 25
    elif c_score == 17:
        mh += 10
        loy += 30
        rea += 30
    elif c_score == 18:
        mh += 15
        loy += 40
        rea += 35
    elif c_score == 19:
        mh += 20
        loy += 50
        rea += 40
    return mh, loy, rea

def calc_wisdom(w_score):
    mst = 0
    if w_score == 3:
        mst += -3
    elif w_score == 4:
        mst += -2
    elif w_score >= 5 or w_score <= 7:
        mst += -1
    elif w_score == 15:
        mst += 1
    elif w_score == 16:
        mst += 2
    elif w_score == 17:
        mst += 3
    elif w_score == 18:
        mst += 4
    elif w_score == 19:
        mst += 5
    return mst