from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired



class RegisterForm(FlaskForm):

      username = StringField(label='UserName:', validators=[Length(min=2, max=30), DataRequired()])
      email_address = StringField(label= 'Email:', validators=[Email(), DataRequired()])
      password1 = PasswordField(label = 'password:', validators=[Length(min=6), DataRequired()]) 
      password2 = PasswordField(label = 'confirm password', validators=[EqualTo('password1'), DataRequired()]) 
      submit = SubmitField(label = 'Create Account')
      