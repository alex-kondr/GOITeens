from flask_wtf import FlaskForm
import wtforms


class ReviewForm(FlaskForm):
    author = wtforms.StringField("Представтесь", validators=[wtforms.validators.length(3), wtforms.validators.DataRequired()])
    text = wtforms.StringField("Введіть свій відгук", validators=[wtforms.validators.length(1), wtforms.validators.DataRequired()])
    grade = wtforms.RadioField("Виберіть свою оцінку")
    submit = wtforms.SubmitField("Зберегти відгук")
