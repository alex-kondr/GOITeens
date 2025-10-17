from flask_wtf import FlaskForm
import wtforms


class SignUpForm(FlaskForm):
    username = wtforms.StringField(
        label="Логін",
        validators=[wtforms.validators.length(min=4), wtforms.validators.DataRequired()]
    )
    first_name = wtforms.StringField(label="Ім'я (за бажанням)")
    last_name = wtforms.StringField(label="Прізвище (за бажанням)")
    password = wtforms.PasswordField(
        label="Пароль",
        validators=[wtforms.validators.length(min=6), wtforms.validators.DataRequired()]
    )
    submit = wtforms.SubmitField(label="Зареєструватись")


class SignInForm(FlaskForm):
    username = wtforms.StringField(
        label="Логін",
        validators=[wtforms.validators.length(min=4), wtforms.validators.DataRequired()]
    )
    password = wtforms.StringField(
        label="Пароль",
        validators=[wtforms.validators.length(min=6), wtforms.validators.DataRequired()]
    )
    submit = wtforms.SubmitField(label="Увійти")


class OrderForm(FlaskForm):
    name = wtforms.SelectField(label="Назва страви", validators=[wtforms.validators.DataRequired()])
    count = wtforms.IntegerField(label="Кількість товару", validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField(label="Додати у замовлення")


class ReservationForm(FlaskForm):
    timastamp = wtforms.DateTimeField(label="Дата та час бронювання столика", validators=[wtforms.validators.DataRequired()])
    table_name = wtforms.IntegerField(label="Номер столика", validators=[wtforms.validators.DataRequired()])
    numbers = wtforms.IntegerField(
        label="Кількість відвідувачів",
        validators=[wtforms.validators.length(min=1), wtforms.validators.DataRequired()]
    )
    submit = wtforms.SubmitField(label="Забронювати")
