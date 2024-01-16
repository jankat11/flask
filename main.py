from flask import Flask
 
app = Flask(__name__)
 
 
@app.route("/")
def index():
    return <p>hello</p>
 
  if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
