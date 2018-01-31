"""
This script is used to check if there are new files then updates the FILE table
and moves them to another folder called "archives"
"""

import mysql.connector
import time
import datetime
import os

fresh_files = './fresh_files/'
files = './files/'
user = 'antonios' #This should change based on the user, will the files stored in the file system have this information?
localtime = time.asctime( time.localtime() )
new_file_name = 'File:%s'%localtime #How is the new name defined? i just used the local time to make it unique
new_file_name = new_file_name.replace(" ", "") #remove spaces

if os.listdir(fresh_files): #check if there are any new files

    for file in os.listdir(fresh_files):

        path_to_file = fresh_files + file
        #command to run vcf_read
        vcf_read_cli = 'python2 vcf_read.py --dbuser antonios  --db dialisi --existing %s --new_file_name %s --new_file_path %s'%(user, new_file_name, path_to_file)
        os.system(vcf_read_cli)

    move_files_cli = 'mv %s* %s'%(fresh_files, files)
    os.system(move_files_cli)
