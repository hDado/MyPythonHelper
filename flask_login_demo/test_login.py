from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import generate_password_hash , check_password_hash
from models import setup_db, User
app = Flask(__name__)
# bcrypt=Bcrypt(app)
setup_db(app)


app.config['SECRET_KEY'] = b'\xb6)aH_\xc1oE\xb0\x1a\x98\x8d\xcb#\x1c\xbe\x8e\xdd~\x93\xd9\xeb\xb8_\xaf\xc2pA\xaa\xe1\x85\xca'


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=30)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=250)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=30)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(user, "user")
        if user:
            print(form.password.data, "form password data")
            print(user.password  ,"----------------")
            hashed = user.password
            original = form.password.data
            if check_password_hash(hashed , original):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


   
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    admin_register_list = ["@trendzmedia.co", "@rocketpage.agency"]
    if form.validate_on_submit():

        if str(form.username.data) in str(admin_register_list) :
            print(form.username.data)
            print(str(admin_register_list))
            hashed_password = generate_password_hash(form.password.data)
            new_user = User(username=form.username.data, password=hashed_password.decode('utf-8'))
            print(new_user.password)
            new_user.insert()
            return redirect(url_for('login'))
        # else:
        #     print("hi there , error")
               
    return render_template('register.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)

