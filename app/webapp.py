####################################
## HARC: (HTML-enabled Analysis of 
##			Replicated CHIPseq)
## A Bioinformatics Project
## High throughput sequencing data
## analysis pipeline development
###################################
## Author: Amanda Holbrook
##	 & Colin Kruse
## Copyright: 2019, HARC
## Version: 1.0.0
## Email: amandajoee@gmail.com
###################################


from flask import Flask, request, url_for, redirect, render_template, flash, session, send_file, send_from_directory, current_app
import pandas as pd
import webbrowser
from threading import Timer
import os, sys, zipfile
from os.path import join, dirname, realpath, abspath
from python.gffGenerator import createGFF
from python.fastaFormatter import formatter
from python.batchRename import rename
from python.countCombiner import merge
app = Flask(__name__)
app.secret_key = "HARC"
# APP_ROOT = dirname(abspath(__file__))
# UPLOAD_FOLDER = join(APP_ROOT, '/static/uploads')

UPLOAD_FOLDER = './tmp/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

RESULTS_FOLDER = app.config['UPLOAD_FOLDER'] + 'results/'
app.config['RESULTS'] = RESULTS_FOLDER

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

if not os.path.exists(app.config['RESULTS']):
	os.makedirs(app.config['RESULTS'])



@app.route('/')
def open_browser():
      webbrowser.open_new('http://127.0.0.1:5000/start')
Timer(1, open_browser).start()
app.run(port=5000)

# route for uploading fasta file
@app.route('/start', methods = ['GET', 'POST']) 
def upload():
	if request.method == 'POST':  
		fastafile = request.files['fastafile']  
		fastafile.save(join((app.config['UPLOAD_FOLDER']), fastafile.filename))
		session['fastaname'] = fastafile.filename
		return redirect("/gff")
	else:
		return render_template('start.html')


# route for converting fasta file
# asks for gff file name and step count
@app.route("/gff", methods=['GET', 'POST'])
def gff():
	verbose = False
	fastafile = session.get('fastaname', "None")
	if request.method == 'POST':
		formatter(join((app.config['UPLOAD_FOLDER']), fastafile), '>', app.config['UPLOAD_FOLDER'])
		formatted = "formatted_" + fastafile
		gff = request.form['gff']
		step = request.form['step']
		createGFF(step, '>', (join((app.config['UPLOAD_FOLDER']), formatted)), gff, verbose, app.config['RESULTS'])
		return redirect('/results')
	else:
		return render_template('gff.html')

#route for renaming a directory/group of files
@app.route('/rename', methods = ['GET', 'POST'])  
def rensub(): 
	if request.method == 'POST':  
		csv = request.files['csv']  
		csv.save(join(app.config['UPLOAD_FOLDER'], csv.filename))
		session['csv'] = csv.filename
		return redirect("/renamesubmit")
	else:
		return render_template('rename.html')

# route for renaming a directory/group of files
@app.route('/renamesubmit', methods=['GET', 'POST'])
def rename2():
	renamepath = app.config['RESULTS'] + 'rename/'
	csvname = session.get('csv', "None")
	csv = app.config['UPLOAD_FOLDER'] + csvname
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
	mergepath = app.config['UPLOAD_FOLDER'] + 'merge/'
	if not os.path.exists(mergepath):
		os.makedirs(mergepath)
	if request.method == 'POST':  
		files = request.files.getlist("merge[]")
		for f in files:
			f.save(os.path.join(mergepath, f.filename))
		return redirect("/combine")
	else:
		return render_template('combinesubmit.html')

#route for combing file counts
#asks for count type, name for merged file, and ext of files to be merged
@app.route("/combine", methods=['GET', 'POST'])
def combine():
	if request.method == 'POST':
		mergepath = app.config['UPLOAD_FOLDER'] + 'merge/'
		mergeby = request.form['mergeby']
		if mergeby == 's':
			col = "Stranded"
		elif mergeby == 'u':
			col = "Unstranded"
		elif mergeby == 'r':
			col = "Reverse"
		mergename = request.form['mergename']
		ext = request.form['ext']
		merge(mergename, col, ext, mergepath, app.config['RESULTS'])
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
	uploads = os.path.join(current_app.root_path, app.config['RESULTS'])
	return send_from_directory(directory=uploads, filename=filename)

# route for project credits
@app.route("/credits")
def credits():
	return render_template('credits.html')

# route for project overview
@app.route("/overview")
def overview():
	return render_template('overview.html')

