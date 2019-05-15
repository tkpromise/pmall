from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('手机号码:', validators=[DataRequired()])
    password = PasswordField('登录密码:', validators=[DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')
