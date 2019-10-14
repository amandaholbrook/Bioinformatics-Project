# HARC

NAME:
    HARC (HTML-enabled Analysis of Replicated CHIPseq)

DEVELOPERS:
    Amanda Holbrook

TECHINCAL ADVISOR:
    Colin Kruse

PRINCIPAL INVESTIGATOR:
    Sarah Wyatt

COPYRIGHT:
    2019

DESCRIPTION:

   High-throughput sequencing dna analysis 
    pipeline development.

FUNCTIONALITY:

   gffGenerator: GFF to fasta conversion,

   fastaFormatter: properly formats fasta file to be read,

   batchRename: file directory renaming,

   countCombiner: combining gene count files

# HOW TO RUN

1. DOWNLOAD FLASK:

        pip install Flask

    Documentation:
    http://flask.palletsprojects.com/en/1.1.x/

2. CLONE THIS REPOSITORY

        git clone https://github.com/amandaholbrook/HARC.git

3. CD INTO APP FOLDER

        cd HARC/app/

4. SET ENVIROMENT VARIABLES

        export FLASK_APP=webapp.py

5. RUN APP

        flask run
