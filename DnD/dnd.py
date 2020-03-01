from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def dnd():
    return render_template('index.html')

@app.route('/find_hero')
def find_hero():
    return render_template('find_hero.html')

if __name__ == "__main__":
    app.run(debug=True)