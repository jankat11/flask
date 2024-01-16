from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/profile')
@app.route('/dashboard')
def hello_world():
    jinja_value = "this is from jinja"
    return render_template("index.html", jinja_value=jinja_value)

if __name__ == '__main__':
    app.run(debug=True)
