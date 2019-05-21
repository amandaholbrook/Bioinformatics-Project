from flask import Flask, request, url_for, redirect, render_template
app = Flask(__name__)

@app.route("/home")
def intro():
	return render_template('home.html')

@app.route("/credits")
def credits():
	if request.method == 'POST':
		fastafile = request.form['fastafile']
		gff = request.form['gff']
		step = request.form['step']
		renamefiles = request.form['renamefiles']
		if renamefiles == true:
			files = request.form['files']
			rename = request.form['rename']
		combinecounts = ['combinecounts']
		if combinecounts == true:
			s = request.form['s']
			u = request.form['u']
			r = request.form['r']
			if s == true:
				col = stranded
			elif u == true:
				col == unstranded
			elif r == true:
				col = reverse
			else:
				return "ERROR: PICK ONLY ONE MERGE TYPE"

			mergename = request.form['mergename']
			ext = request.form['ext']
	else:
		return render_template('credits.html')

	#@app.route('\database', methods=['GET', 'POST'])
	#def database():
	#	query = []
	#	for i in session.quesrt(models.)