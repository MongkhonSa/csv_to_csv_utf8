import pandas as pd
import pathlib
import chardet 
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

# define the pattern
currentPattern = "raw_data/*.csv"
for currentFile in currentDirectory.glob(currentPattern):  
	str_currentFile = str(currentFile)
	my_encoding = find_encoding(str_currentFile)
	# print(str_currentFile)
	df = pd.read_csv(io.open(str_currentFile,encoding=my_encoding, errors='ignore'))
	# print(df.columns)
	csv_utf_8=str_currentFile.replace("raw_data","csv_utf_8")
	df.to_csv(path_or_buf=csv_utf_8, encoding='UTF-8-SIG',index=False)
	
	