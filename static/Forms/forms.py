from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class WatchListForm(FlaskForm):
    WlName = StringField('Watch List Name:', validators=[DataRequired()])
    # Length(min=1, max=15)])
