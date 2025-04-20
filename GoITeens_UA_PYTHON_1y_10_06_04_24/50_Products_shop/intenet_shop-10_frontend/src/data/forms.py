from flask_wtf import FlaskForm
import wtforms


class ReviewForm(FlaskForm):
    text = wtforms.StringField("Введіть свій відгук про даний товар", validators=[wtforms.validators.length(5, message="Відгук занадто короткий")])
    name = wtforms.StringField("Введіть своє ім'я", validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Зберегти")
