from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def hello():
  return render_template('login.html')


@app.route("/home")
def home():

	if request.method=='POST':

		username=request.form['username']
		password=request.form['password']
		print("hello  i m in inside post2")
		sql ="insert into users(username,password) values('{}','{}')".format(username,password)
		cursor.execute(sql)
		db.commit()		# Commit your changes in the database
		data=cursor.fetchone()
	return 	redirect(url_for('login'))
if __name__== "__main__":
  app.run(host="0.0.0.0", port=int("5000"), debug=True)
