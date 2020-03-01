import dnd_db
from flask import Flask, render_template, url_for, request
from dnd_extensions import mongo_client
from dnd_forms import FindHeroForm

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def dnd():
    return render_template('index.html')

@app.route('/find_hero', methods=["GET", "POST"])
def find_hero():
    if request.method == "POST":
        form = forms.FindHeroForm()
        mdb = mongo_client.OSRIC
        heroes = dnd_db.display_name(mdb, orm.character_name.data)
    return render_template('find_hero.html', heroes)

if __name__ == "__main__":
    app.run(debug=True)