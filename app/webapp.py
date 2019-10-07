from flask import Flask, request, url_for, redirect, render_template, flash, session, send_file, send_from_directory, current_app
import pandas as pd
import os, sys, zipfile
from python.gffGenerator import createGFF
from python.fastaFormatter import formatter
from python.batchRename import rename
from python.countCombiner import merge
app = Flask(__name__)
app.secret_key = "HARC"
UPLOAD_FOLDER = '/HARCfiles'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

path = './HARCtemp/'
if not os.path.exists(path):
	os.mkdir(path)

results = path + 'results/'
if not os.path.exists(results):
	os.mkdir(results)

# route for uploading fasta file
@app.route('/start', methods = ['GET', 'POST'])  
def upload():  
	path = './HARCtemp/'
	if request.method == 'POST':  
		fastafile = request.files['fastafile']  
		fastafile.save(os.path.join(path, fastafile.filename))
		session['fastaname'] = fastafile.filename
		return redirect("/gff")
	else:
		return render_template('start.html')


# route for converting fasta file
# asks for gff file name and step count
@app.route("/gff", methods=['GET', 'POST'])
def gff():
	path = './HARCtemp/'
	results = path + 'results/'
	if not os.path.exists(results):
		os.mkdir(results)
	verbose = False
	fastafile = session.get('fastaname', "None")
	if request.method == 'POST':
		formatter(path + fastafile, '>', path)
		gff = request.form['gff']
		step = request.form['step']
		createGFF(step, '>', path+fastafile, gff, verbose, results)
		return redirect('/results')
	else:
		return render_template('gff.html')

#route for renaming a directory/group of files
@app.route('/rename', methods = ['GET', 'POST'])  
def rensub():  
	path = './HARCtemp/'
	if request.method == 'POST':  
		csv = request.files['csv']  
		csv.save(os.path.join(path, csv.filename))
		session['csv'] = csv.filename
		return redirect("/renamesubmit")
	else:
		return render_template('rename.html')

# route for renaming a directory/group of files
@app.route('/renamesubmit', methods=['GET', 'POST'])
def rename2():
	path = './HARCtemp/'
	results = path + 'results/' 
	renamepath = results + 'rename/'
	csvname = session.get('csv', "None")
	csv = path + csvname
	if not os.path.exists(renamepath):
		os.mkdir(renamepath)
	if request.method == 'POST':  
		files = request.files.getlist("rename[]")
		for f in files:
			f.save(os.path.join(renamepath, f.filename))
		rename(csv, renamepath)
		return redirect('/results')
	else:
		return render_template('renamesubmit.html')

#route for uploading files to combine the counts
@app.route('/combinesubmit', methods = ['GET', 'POST'])  
def comsub():  
	path = './HARCtemp/'
	mergepath = path + 'merge/'
	if not os.path.exists(mergepath):
		os.mkdir(mergepath)
	if request.method == 'POST':  
		files = request.files.getlist("merge[]")
		for f in files:
			f.save(os.path.join(path, f.filename))
		return redirect("/combine")
	else:
		return render_template('combinesubmit.html')

#route for combing file counts
#asks for count type, name for merged file, and ext of files to be merged
@app.route("/combine", methods=['GET', 'POST'])
def combine():
	path = './HARCtemp/'
	results = path + 'results/'
	if request.method == 'POST':
		mergepath = path + 'merge/'
		mergeby = request.form['mergeby']
		if mergeby == 's':
			col = "Stranded"
		elif mergeby == 'u':
			col = "Unstranded"
		elif mergeby == 'r':
			col = "Reverse"
		mergename = request.form['mergename']
		ext = request.form['ext']
		merge(mergename, col, ext, mergepath, results)
		return redirect('/results')
	else:
		return render_template('combine.html')


# route for results page
# from here the user can do anotehr conversion, or chose to do another taskx
@app.route("/results")
def results():
	return render_template('results.html')

@app.route("/download")
def download():
	filename = session.get['download']
	uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
	return send_from_directory(directory=uploads, filename=filename)

# route for project credits
@app.route("/credits")
def credits():
	return render_template('credits.html')

# route for project overview
@app.route("/overview")
def overview():
	return render_template('overview.html')

