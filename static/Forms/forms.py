from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField
from wtforms.validators import DataRequired


class WatchListForm(FlaskForm):
    WlName = StringField('Watch List Name:', validators=[DataRequired()])


class WatchListContentsForm(FlaskForm):
    WlId = IntegerField('Enter Watch List ID:', validators=[DataRequired()])


class StockForm(FlaskForm):
    Ticker = StringField('Add stock via Ticker:', validators=[DataRequired()])

