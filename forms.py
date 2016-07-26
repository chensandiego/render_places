from flask_wtf import Form 
from wtforms import StringField,PasswordField,SubmitField 
from wtforms.validators import DataRequired,Email,Length

class SignupForm(Form):
	first_name = StringField('First Name',validators=[DataRequired('Please enter your first name')])
	last_name = StringField('Last Name',validators=[DataRequired('Please enter your last name')])
	email = StringField('Email',validators=[DataRequired(),Email('please enter valid email')])
	password = PasswordField('Password',validators=[DataRequired(),Length(min=6,message="Password must be at least 6 characters")])
	submit=SubmitField('Sign up')



class LoginForm(Form):
	email = StringField("Email",validators=[DataRequired("please enter your email"),Email("please enter your email address")])
	password = PasswordField('Password',validators=[DataRequired("Please enter a password")])
	submit = SubmitField("Sign in")


class AddressForm(Form):
	address = StringField('Address',validators=[DataRequired("Please enter an address")])
	submit = SubmitField("Search")