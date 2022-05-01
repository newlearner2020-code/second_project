#import render template to attach html files with main pyton file
from flask import Flask, render_template
#the bootstrap made for flask
from flask_bootstrap import Bootstrap
# wtf is use for forms creation and validation
from flask_wtf import FlaskForm
#import field for string and password
from wtforms import StringField, PasswordField
#import validators for form
from wtforms.validators import InputRequired, length, DataRequired

app = Flask(__name__)
#the secret key use sequrity reason and prevent attacks
app.config['SECRET_KEY'] = 'v4dsv6svs4v+56'
Bootstrap(app)

#making a class for login form having e-mail and password
class loginform(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[InputRequired(), length(min=8, max=16)])

#making a class for Signup form having username,password and email
class Signup(FlaskForm):
    username = StringField('username', validators=[DataRequired(), length(min=4, max=12)])
    user_email = StringField('email', validators=[InputRequired()])
    user_password = PasswordField('password', validators=[InputRequired(), length(min=8, max=16)])


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login/", methods=['GET', 'POST'])
def login():
    #making a form var that represent login class
    form = loginform()
    if form.validate_on_submit():
        return '<h1>' + form.email.data + ' ' + form.password.data + '</h1>'
#attaching thelogin.html with login fuction
    return render_template("login.html", form=form)


@app.route("/signup/", methods=['GET', 'POST'])
def signup():
    form = Signup()
    if form.validate_on_submit():
        return '<h1>' + form.username.data + '</h1>'
    return render_template("signin.html", form=form)


@app.route("/Models/")
def models():
    return render_template("models.html")


if __name__ == "__main__":
    app.run(debug=True)
