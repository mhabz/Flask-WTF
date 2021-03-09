from flask import Flask, render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, AnyOf

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
app.config['RECAPTCHA_PUBLIC_KEY']='6Le1P3gaAAAAABqz2Zya77yOZuqN5_VR9TFJB9qV'
app.config['RECAPTCHA_PRIVATE_KEY']='6Le1P3gaAAAAAG8hL3egNZh6UxcWSuQSvCXgrNkp'
app.config['TESTING']=False

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(message = 'A username is requierd' ),Length(min=5, max=50, message='Must be between 5 and 10 characters.')])
    password = PasswordField('password', validators=[InputRequired('Password is required!'), AnyOf(values=['password', 'secret'])])
    recaptcha = RecaptchaField()

@app.route('/form', methods =['GET', 'POST'])
def form():
    form = LoginForm()

    if form.validate_on_submit():
        return '<h2> The username is {}. The passwd  is {} '.format(form.username.data, form.password.data)
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
