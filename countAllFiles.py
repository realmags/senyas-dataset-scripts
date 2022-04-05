import os
import pprint

# directory path
working_dir = './'

# count total subdirectories
total_files_per_dir = [[root, len(files)] for root, _, files in os.walk(working_dir)]

# display total
pprint.pprint(total_files_per_dir)
