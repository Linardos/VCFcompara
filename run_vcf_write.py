"""
This script is used to check if there are new tasks in the ANALYSES table,
runs them and updates the timestamp
"""
#Current Issues:
#1. Matching the user that makes the query.
#2. I don't know why metadata is needed in vcf_write but it doesnt run without it


import mysql.connector
import time
import datetime
import os

folder = './files/'
user = 'antonios'

db = mysql.connector.connect(user='antonios', database='dialisi')

#Check for new tasks using the NULL timestamp as a criteria
search_tasks_query = ("SELECT * FROM ANALYSES WHERE start_time is NULL")
#create a cursor to execute the command in the database
cur = db.cursor(dictionary=True)
cur.execute(search_tasks_query)
for task in cur:
    #print(len(timestamp))

    analysis_id = task['analysis_id']
    file_id_1 = task['file_id_1']
    file_id_2 = task['file_id_2']
    analysis_type = task['analysis_type']
    output_file_name = task['output_file_name']

    #add starting time to the table
    cur_start_time = db.cursor(buffered=True)
    update_time = 'UPDATE ANALYSES SET start_time = now() WHERE analysis_id = %i'%(analysis_id)
    cur_start_time.execute(update_time)
    db.commit()

    #match the ids to the unique file names:
    cur2 = db.cursor(buffered=True, dictionary=True)
    match_files = ("SELECT file_name FROM FILE WHERE file_id = %i or %i"%(file_id_1, file_id_2))
    cur2.execute(match_files)

    #fetch the names
    file_names = cur2.fetchall()
    file_name_1, file_name_2 = file_names[0]['file_name'], file_names[1]['file_name']

    #run the analysis
    vcf_write_cli = 'python2 vcf_write.py --dbuser antonios --db dialisi --site_user %s --job %s --out_file %s --file1 %s --file2 %s --metadata ./files/danio_rerio.vcf'%(user, analysis_type, output_file_name, file_name_1, file_name_2)
    os.system(vcf_write_cli)


    #add ending time to the table
    cur_end_time = db.cursor(buffered=True)
    update_time = 'UPDATE ANALYSES SET end_time = now() WHERE analysis_id = %i'%(analysis_id)
    cur_end_time.execute(update_time)
    db.commit()
