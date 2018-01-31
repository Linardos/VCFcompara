"""
This script is used to check if there are new files then updates the FILE table
and moves them to another folder called "archives"
"""

import mysql.connector
import time
import datetime
import os

fresh_files = './fresh_files/'
archives = './archives/'
user = 'antonios' #This should change based on the user, will the files stored in the file system have this information?

ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
#print(len(timestamp))

if os.listdir(fresh_files): #check if there are any new files

    for file in os.listdir(fresh_files):

        path_to_file = fresh_files + file
        db = mysql.connector.connect(user='antonios', database='dialisi')

        #create a cursor for the select
        cur = db.cursor()
        search_user_query = ("SELECT user_id FROM USER WHERE username = %s")
        cur.execute(search_user_query, (user,))
        vcf_read_cli = 'python2 vcf_read.py --dbuser antonios  --db dialisi --existing %s --new_file_name atest2 --new_file_path %s'%(user, path_to_file)
        os.system(vcf_read_cli)

    os.system('mv ./fresh_files/* ./archives/')
