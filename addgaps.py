#! python3
#addgaps.py Will add a gap in a series of files
#works for file names such as spam001.txt, spam002.txt etc

import os, re, shutil

def add_gaps(folder,spot_number):
#TODO: get the folder path and a list of the files
    cur_folder = os.path.abspath(folder)
    print(cur_folder)
    list_of_files = os.listdir(folder)
    print(list_of_files)

    #create regex for file and numbering system
    filename_regex = re.compile(r'^([a-zA-Z]*)([0-9][0-9][0-9])(.*)$')
    mo_prefix = filename_regex.search(list_of_files[1])
    print(filename_regex.search(list_of_files[1]))



#TODO: Change the filenames proceeding the gap to match the gap
    for files in list_of_files[:spot_number-2:-1]:

        mo = filename_regex.search(files)
        prefix = mo.group(1)
        numbering = mo.group(2)
        suffix = mo.group(3)
        cur_name = prefix+numbering+suffix
        print(cur_name.center(15,'~'))
        next_number = int(numbering) + 1
        new_name = prefix+(str(next_number)).zfill(3)+suffix
        print('is now -> ' + str(new_name) +'\n')

#change the file names of the prceeding files
        
##        shutil.move(os.path.join(cur_folder,cur_name),os.path.join(cur_folder,str(new_name)))
    print('done')
    print(os.listdir(folder))
        

add_gaps('c:\\test',7)
