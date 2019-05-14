from flask import Flask, request, url_for, redirect, render_template
app = Flask(__name__)

@app.route("/home")
def intro():
	return render_template('home.html')

@app.route("/credits")
def credits():
	return render_template('credits.html')