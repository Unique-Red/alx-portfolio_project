from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home page"

@app.route("/signin")
def signin():
    return "Signin page"

@app.route("/signup")
def signup():
    return "Signup page"

if __name__ == "__main__":
    app.run()