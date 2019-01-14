from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class forms(FlaskForm):
	firstname = StringField('First Name', validators=[DataRequired(), Length(min=1, max=40)])
	lastname = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=40)])
	gender = StringField('Gender', validators=[DataRequired(), Length(min=1, max=15)])
	year = StringField('Year Level', validators=[DataRequired(), Length(min=1, max=15)])
	course = StringField('Course', validators=[DataRequired(), Length(min=1, max=100)])

class Course(FlaskForm):
	course = StringField('Course Name', validators=[DataRequired(), Length(min=1, max=100)])
	code = StringField('Code', validators=[DataRequired(), Length(min=1, max=20)])

class SearchForm(FlaskForm):
	student = StringField('Student')
	course = StringField('Course')    
