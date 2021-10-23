from flask_wtf import Form, FlaskForm
from wtforms.widgets import TextArea
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import NumberRange



class InputForm(FlaskForm):
    submit_field = SubmitField('Encode')
    input_field = StringField(
        label='Input Field', description="db_enter", widget=TextArea())


class OutputForm(FlaskForm):
    output_field = StringField(label='Output Field', widget=TextArea())


class RetrieveDBInfo(Form):
    numRetrieve = IntegerField(
        label='Number of DB Items to Get', description="db_get", validators=[NumberRange(min=0, max=100)])
    submit_field = SubmitField('Retrieve')
