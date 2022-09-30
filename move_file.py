import os
import shutil

from_dir = "C:/Users/mitul/Desktop/Mahek Projects/sampleFolder"
to_dir = "C:/Users/mitul/Desktop/Mahek Projects/pngFile"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file in list_of_files:

    name, extension = os.path.splitext(file)

    if extension == '':
        continue

    if extension in ['.txt' , '.doc' , '.docx' , '.pdf']:
        path1 = from_dir + '/' + file
        path2 = to_dir + '/' + "Document_files" 
        path3 = to_dir + '/' + "Document_files" + '/' + file

        if os.path.exists(path2):
            shutil.move(path1 , path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)