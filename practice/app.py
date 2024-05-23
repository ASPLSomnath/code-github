from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/')
def name():
	return render_template('som.html')

@app.route('/place')
def place():
	return render_template('place.html')




if __name__ == "__main__":
	app.run(debug=True)