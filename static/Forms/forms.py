from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class WatchListForm(FlaskForm):
    WlName = StringField('Watch List Name:', validators=[DataRequired()])
    # Length(min=1, max=15)])


class WatchListContentsForm(FlaskForm):
    WlId = IntegerField('Watch List ID:', validators=[DataRequired()])


class AddStockForm(FlaskForm):
    Ticker = StringField('Stock Ticker:', validators=[DataRequired()])
