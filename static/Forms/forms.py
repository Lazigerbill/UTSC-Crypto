from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Optional


class WatchListForm(FlaskForm):
    WlName = StringField('Watch List Name:', validators=[DataRequired()])
    # Length(min=1, max=15)])


class WatchListContentsForm(FlaskForm):
    WlId = IntegerField('Watch List ID:', validators=[DataRequired()])


class StockForm(FlaskForm):
    Ticker = StringField('Add stock via Ticker:', validators=[DataRequired()])

