from flask import Flask, request, url_for, redirect, render_template
import pandas as pd
import os
from gffGenerator import createGFF
from fastaFormatter import formatter
from batchRename import rename
app = Flask(__name__)


@app.route("/home", methods=['GET', 'POST'])
def getinput():
	path = './results'
	if request.method == 'POST':
		if not os.path.exists(path):
			os.mkdir(path)
		# fastafile = request.form['fastafile']
		# formatter(fastafile, '>', path)
		# gff = request.form['gff']
		# step = request.form['step']
		# createGFF(step, '>', path+fastafile, gff, verbose, './')
		# renamefiles = request.form['renamefiles']
		if renamefiles == true:
			renamepath = './results/rename'
			if not os.path.exists(renamepath):
		 		os.mkdir(renamepath)
			files = request.form['files']
			rename = request.form['rename']
			os.system('cp -r ' + files + " " + path)
		# rename(renamepath, rename)
		# combinecounts = ['combinecounts']
		# if combinecounts == true:
		# 	s = request.form['s']
		# 	u = request.form['u']
		# 	r = request.form['r']
		# 	if s == true:
		# 		col = stranded
		# 	elif u == true:
		# 		col == unstranded
		# 	elif r == true:
		# 		col = reverse
		# 	else:
		# 		return "ERROR: PICK ONLY ONE MERGE TYPE"
		# 	mergefiles = request.form['mergefiles']
		# 	mergename = request.form['mergename']
		# 	ext = request.form['ext']
		# 	combine(mergename, col, ext, mergefiles)
		return redirect('/results')
	else:
		return render_template('home.html')

@app.route("/credits")
def credits():
	return render_template('credits.html')

@app.route("/overview")
def overview():
	return render_template('overview.html')

@app.route('/results')
def results():
	return "Results."