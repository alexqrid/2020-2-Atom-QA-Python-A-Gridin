from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "iliya": generate_password_hash('123'),
    "kirill": generate_password_hash('321'),
    "yar": generate_password_hash('333')
}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route('/')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())


@app.route('/profile')
@auth.login_required
def profile():
    return "{}, this is your profile!".format(auth.current_user())


@app.route('/photo')
@auth.login_required
def photo():
    return 'Photo'


@app.route('/shareware')
def shareware():
    return 'Free for all!'


@app.route('/logout')
@auth.login_required
def logout():
    return f"{auth.current_user()} was logout!", 401


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5555)
