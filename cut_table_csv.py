import pandas as pd
import pathlib
import chardet 
import csv
import sys,io
sys._enablelegacywindowsfsencoding()
sys.getfilesystemencoding()
def find_encoding(fname):
    r_file = open(fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc
 
# define the path
currentDirectory = pathlib.Path('.')
currentPattern = "raw_data/*.csv"
for currentFile in currentDirectory.glob(currentPattern):  

    temp =[]
    str_currentFile = str(currentFile)
    print("converting.. "+str_currentFile,end=" ")
    my_encoding = find_encoding(str_currentFile)
    csv_utf_8_path=str_currentFile.replace("raw_data","csv_utf_8")
    with open(str_currentFile,encoding=my_encoding, errors='ignore') as myFile:  
        reader = csv.reader(myFile)
        for row in reader:
            check_row_value =0
            for col in row:
                if(col):
                    check_row_value=check_row_value+1
            # row = tuple("=\"" + r + "\"" for r in row) # เพิ่มมาแก้ leading 0
            if check_row_value>1:
                temp.append(row)
				
				

    output = open(csv_utf_8_path, 'w',newline='', encoding='utf-8-sig')  
    with output:  
        writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(temp)
    print("save as .."+str(csv_utf_8_path))