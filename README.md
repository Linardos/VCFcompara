# cron-jobs

The run_vcf_read script uses 2 folders in order to separate the newly uploaded files from the ones that have been parsed by vcf_read.
So newly uploaded files should first be stored to the folder "fresh_files", the script will parse them and move them to the folder "files".

The run_vcf_write script checks if there are any tasks with NULL start time in the ANALYSES table. Then runs the vcf_write based on the instructions of each task and updates the time.

cron_script sets each file to run once per minute
