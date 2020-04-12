from flask import Flask, Blueprint
from auth import auth
from profile import profile
from sozluk import sozluk

app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(profile)
app.register_blueprint(sozluk)
if __name__ == "__main__":
    app.secret_key = "^A%DJAJU^JJ123"
    app.run(debug=True)