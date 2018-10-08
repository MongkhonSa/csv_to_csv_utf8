import csv
temp =[]
with open("01.csv",encoding="TIS-620") as myFile:  
    reader = csv.reader(myFile)
    for row in reader:
      temp.append(row)
    
    

output = open("file_utf8.csv", 'w',newline='', encoding='utf-8-sig')  
with output:  
    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerows(temp)