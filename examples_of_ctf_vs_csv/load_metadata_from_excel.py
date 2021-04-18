#import xlrd
import json
import csv 

with open("template_ctf.json") as file:
    json_data = json.load(file)
    
default_column = json_data["tableSchema"]["columnFiles"][0]

print(default_column) 

arr = []

with open("GDELT_2.0_Events_Column_Labels_Header_Row_Sep2016.csv") as csv_file:
    next(csv_file) #skip the first line since it is the header
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        arr.append(row[1].lower())

#print(arr)

"""
book = xlrd.open_workbook("myfile.xls")
sh = book.sheet_by_index(0)
"""
print(json_data["tableSchema"]["columnFiles"])

#print(default_column)
empty = []
new_column = default_column 
for i in range(0,61):
    #new_column = default_column
    new_column["url"] = "column" + str(i+1) + ".txt"
    new_column["datatype"]["base"] = arr[i] #sh.cell_value(2, i)
    #print(new_column)
    #json_data["tableSchema"]["columnFiles"].append(new_column)
    empty.append(new_column) 
    #json_data["tableSchema"]["column" + str(i+1) + ".txt"] = arr[i]

#print(json_data["tableSchema"]["columnFiles"])
print(empty)

"""
out_json = json.dumps(json_data, indent=4, sort_keys=True)

with open("newFile") as file:
    file.write(out_json)

"""
