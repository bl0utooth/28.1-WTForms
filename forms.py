from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, URL
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bluprint'

class AddPetForm(FlaskForm):
    name = StringField('Pet Name', validators = [InputRequired()])
    species = StringField('Species', validators = [InputRequired()])
    photo_url = StringField('Photo URL', validators = [URL()])
    age = IntegerField('Age')
    notes = TextAreaField('Notes')
    available = BooleanField('Available for Adoption')

class EditPetForm(FlaskForm):
    photo_url = StringField('Photo URL', validators = [InputRequired(), URL()])
    notes = TextAreaField('Notes', validators = [InputRequired()])
    available = BooleanField('Available for Adoption')