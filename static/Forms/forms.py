from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class TickerForm(FlaskForm):
    ticker = StringField('ticker', validators=[DataRequired()])
    # Length(min=1, max=15)])
