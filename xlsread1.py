# python
# The basic skill of open files
# There is the way to read files that identified path.
# 1. use 'sys' module to get operator dlls to get identified path.
# 2. sys.argv[0] is your programm, and argv[1] is the path.
# 3. use 'os' and 'glob' module to read multi-files.

import os
import sys
import glob
import csv
import random
from datetime import date
from xlrd import open_workbook
from xlwt import Workbook

def display(raw):    
    i=0
    raw_list=raw.split(',')
    for data in raw_list :
        #Get the date and delete the time.        
        print ('{}. {}'.format(i,data))
        i=i+1               
    #Get the total texts.

    #get readnumber.

    #merge next 3 colum to get comment number

    #keep the linkage

    #writ to files.
    
    return True

def baddata(bad_lists):
    return False
    #print ("Now we found {} lines data have problems! ".format(len(bad_lists)))
    #print ("They are: {}.\n".format(bad_lists))
    # with open('errofile.csv','w') as ef:
        

def readfile2(infile):
    with open(infile, 'r') as fr:
        i =1
        j =1
        for raw in fr:            
            print ("Read {} .....send it to anlyist!\n".format(raw.strip()))
            if i ==1:
                i=i+1
                print ("Read Title: \n {}\n".format(raw.strip()))
                continue
            i=i+1
            display(raw)
        print ("Total read {} lines.".format(i))
        print ("Total misanalised is {} lines.".format(j))
    
def readfile(infile):
    with open(infile, 'r') as fr:
        i=1
        for raw in fr:            
            print ("Read {} .....send it to anlyist!\n".format(raw.strip()))
            i=i+1            
        print ("Total read {} lines.".format(i))
    
def csvRead(infile):
    with open(infile,'r') as fr:
        filereader = csv.reader(fr)
        i=1
        for raw in filereader:
            print ("Read files #{}.\t".format(i))
            print ("Context: {}.".format(raw))
            i=i+1
        print ("Total read {} lines.".format(i))
        
def xlsxRead(infile,i):
    out1 = "out"+ str(i)
    output_file = out1+".xls"
    output_workbook =Workbook()
    output_worksheet =output_workbook.add_sheet('Result01')
    with open_workbook(infile) as workbook:
        print("Number of worksheets: ",workbook.nsheets)
        for worksheet in workbook.sheets():
            if worksheet.name =='Sheet1':
                for row_index in range(worksheet.nrows):
                    act_num=0
                    for col_index in range(worksheet.ncols):
                        if col_index == 0:
                            if worksheet.cell_type ==3:
                                d1 = xldate_as_tuple(worksheet.cell_value(row_index,col_index),workbook.datemode)
                                d1= date(*date_cell[0:3].strftime('%Y-%m-%d'))
                            else:
                                d1 = str(worksheet.cell_value(row_index, col_index)).split()[0]
                            output_worksheet.write(row_index,col_index,d1)
                        if col_index == 1:
                            d2 = worksheet.cell_value(row_index, col_index)
                            output_worksheet.write(row_index,3,d2)
                        if col_index == 2:
                            d3 = worksheet.cell_value(row_index, col_index)
                            output_worksheet.write(row_index,6,d3)
                        if col_index == 3:
                            d3 = worksheet.cell_value(row_index, col_index)
                            output_worksheet.write(row_index,5,d3)
                        if col_index == 4:
                            if worksheet.cell_type(row_index,col_index) == 2:
                                act_num= act_num + worksheet.cell_value(row_index,col_index)
                        if col_index == 5:
                            if worksheet.cell_type(row_index,col_index) == 2:
                                act_num= act_num + worksheet.cell_value(row_index,col_index)
                        if col_index == 6:
                            if row_index == 0:
                                output_worksheet.write(row_index,7,"互动量")                                
                            else:
                                if worksheet.cell_type==2:
                                    act_num= act_num + worksheet.cell_value(row_index,col_index)
                                output_worksheet.write(row_index,7,act_num)                            
                        if col_index == 7:
                            d4 = worksheet.cell_value(row_index, col_index)
                            output_worksheet.write(row_index,4,d4)
    output_workbook.save(output_file)                           
                        #print("Worksheet Row: ",row_index, ", \tcol: ",col_index,", \tType: ",worksheet.cell_type(row_index,col_index))
                        #print("The cell value is: ",worksheet.cell_value(row_index,col_index))
                

inputPath ='./data' 
#sys.argv[1]
inputName = "*.xlsx"
file_lists = glob.glob(os.path.join(inputPath,inputName))
print ('# Output #1: foud {} files. \n'.format(len(file_lists)))
print ("# Output #2: The file reader! {}\n\t".format(file_lists))
i=0
for infile in file_lists:
    print ("Found {}, and send to read this file.\n\t".format(infile))
    #readfile(infile)
    #csvRead(infile)
    i = i+1
    xlsxRead(infile,i)
    
