
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices = [('dog', 'Dog'), ('cat', 'Cat'), ('fish', 'Fish'), ('hamster','Hamster'), ('snake','Snake')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = FloatField("Age", validators=[NumberRange(min=0,max=30, message='Age must be under 30.')])
    notes = TextAreaField("Notes", validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Is this pet available?")