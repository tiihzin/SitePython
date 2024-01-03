from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/users/<username>')
def users(username):
    return render_template('user.html', username = username)


if __name__ == "__main__":
    app.run(debug=True)
    