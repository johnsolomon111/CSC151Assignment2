from flask import Flask, render_template, request, url_for, redirect
import mysql.connector
from mysql.connector import errorcode
from forms import forms, Course, SearchForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfgh'

mydb = mysql.connector.connect(user='root',password='jonsol109811',host="127.0.0.1",database='studentdb2')

mycursor = mydb.cursor(dictionary=True)

@app.route('/', methods=['POST','GET'])
def index():
	searchForm = SearchForm()
	mycursor.execute("SELECT id,firstname,lastname,gender,course,year FROM student")
	data = mycursor.fetchall()
	return render_template('index.html', data=data, title='Assignment', searchForm=searchForm)

@app.route('/add',methods=['POST','GET'])
def add():
	form = forms(request.form)
	if request.method == 'POST':
		firstname = request.form['firstname']
		lastname = request.form['lastname']
		gender = request.form['gender']
		course = request.form['course']
		year = request.form['year']
		val = (firstname,lastname,gender,course,year)
		sql = "INSERT INTO student (firstname,lastname,gender,course,year) VALUES (%s, %s, %s, %s, %s)"
		mycursor.execute(sql, val)
		mydb.commit()
		return redirect(url_for('index'))

	return render_template('addform.html',form=form , title='Add')

@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete(id):
	sql = "DELETE FROM student WHERE id="+id
	# val = (id)
	mycursor.execute(sql)
	mydb.commit()
		
	return redirect(url_for('index'))

@app.route('/update/<string:id>', methods=['POST', 'GET'])
def update(id):
	sql1 = "SELECT id,firstname,lastname,gender,course,year FROM student WHERE id="+id
	mycursor.execute(sql1)
	data = mycursor.fetchone()

	form = forms(request.form)
	if request.method == 'POST':
		
		firstname = request.form['firstname']
		lastname = request.form['lastname']
		gender = request.form['gender']
		course = request.form['course']
		year = request.form['year']
		val = (firstname,lastname,gender,course,year)
		sql = "UPDATE student SET firstname=%s,lastname=%s,gender=%s,course=%s,year=%s WHERE id="+str(id)
		mycursor.execute(sql, val)
		mydb.commit()
		return redirect(url_for('index'))
 
	return render_template('update.html', form=form, data=data)

@app.route('/search', methods=['POST', 'GET'])
def search():
	searchForm = SearchForm()
	if request.method == 'POST' and searchForm.validate_on_submit():
		student = request.form['student']
		sql = '''SELECT * FROM student WHERE firstname LIKE "%'''+student+'''%" or lastname LIKE "%'''+student+'''%"'''
		mycursor.execute(sql) 
		result = mycursor.fetchall()
		return render_template('searchresults.html', searchForm=searchForm, result=result)
	return render_template('index.html', searchForm=searchForm)

if __name__ == '__main__':
	app.run(debug=True)
