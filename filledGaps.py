#! python3
#fillGaps.py Will find gaps in file names with prefixes and fill them in
#works for file names such as spam001.txt, spam003.txt, etc

import os, re, shutil

def filled_gaps(folder, prefix):

    #Getting the folder path and the list of files in that folder
    print(folder)
    cur_folder = os.path.abspath(folder)
    print(cur_folder)
    list_of_files = os.listdir(cur_folder)

    #Creating a regex to separate the prefix and suffix from the numbers
    filename_regex = re.compile(r'^([a-zA-Z]*)([0-9][0-9][0-9])(.*)$')
    mo_prefix = filename_regex.search(list_of_files[1])

    #creating a list with the correctly ordered and non-gapped file list
    real_number_inc = 1
    real_number = []
    for items in range(len(list_of_files)):
        real_number.append(str(prefix)+str(real_number_inc).zfill(3)+mo_prefix.group(3))
        real_number_inc += 1

    #user regex to separate current file list into regex groups
    i = 0
    for files in list_of_files:
        
        mo = filename_regex.search(files)
        prefix = mo.group(1)
        numbering = mo.group(2)
        ending = mo.group(3)
        cur_name = prefix+numbering+ending

    
    #TODO: Check if there is a gap
        if cur_name != real_number[i]:
            print(str(real_number[i]) + ' file not found')
            shutil.move(os.path.join(cur_folder,cur_name), os.path.join(cur_folder,real_number[i]))
            print('changing ' + str(cur_name) + ' to ' + str(real_number[i]))
            i += 1
        else:
            print(str(cur_name) + ' ok')
            i += 1
    print('done')



p = 'c:\\test'
filled_gaps(p,'test')
