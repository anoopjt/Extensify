#!/usr/bin/python
#------------------------------------------------------------------
#Author: Anoop Jacob Thomas                                       |
#Email: anoopjt@gmail.com                                         |
#Website: http://anoop.caremedia.org                              |
#License: GNU GPL 3.0 or any later you choose                     |
#-----------------------------------------------------------------|
#The program 'extensify' determines the extension of all files in |
#the current working directory and adds the extension to it.      |
#It makes an assumption that if a '.' exist in a file name it     |
#already has an extension and thus does not add extension.        |
#'Extensify' is provided with no warranty or anything.            |
#------------------------------------------------------------------

import time
import mimetypes
import os

if __name__ == "__main__":
    cwd_py=os.getcwd()
    mimetypes.init()
    mimetypes.knownfiles
    #print mimetypes.types_map['.tgz']
    #print mimetypes.guess_type(cwd_py + '/1')
    dir_list=os.listdir(os.getcwd())
    for files in dir_list:
        #print files
        if " " in files:
            new_file_name_list = files.split(" ")
            files=""
            for words in new_file_name_list:
                if files == "":
                    files = words
                else:
                    files = files + '\ ' + words
        f_handler = os.popen('file -bi ' + files , 'r')
        file_type=f_handler.read().split(';') #earlier this was "\n"
        file_type=file_type[0]
        #print file_type
        f_handler.close()
        file_extension=mimetypes.guess_extension(file_type)
        if file_extension != None:
            if file_extension == ".jpe":
                file_extension = ".jpg"
            #print file_type    + ' -> ' + files + ' -> ' + file_extension
            if '.' not in files and file_extension != ".obj":
                if os.path.exists(files+file_extension):
                    local_time=time.localtime()
                    time_in_str = str(local_time[0]) + '-' + str(local_time[1]) + '-' + str(local_time[2]) + '-' + str(local_time[3]) + '-' + str(local_time[4])
                    os.system('mv ' + files + ' ' + files + '-extensified-' + time_in_str +file_extension)
                    print 'Renaming file ' + files + ' to ' + files + '-extensified-' + time_in_str + file_extension
                else:
                    os.system('mv ' + files + ' ' + files + file_extension)
                    print 'Renaming file ' + files + ' to ' + files + file_extension
