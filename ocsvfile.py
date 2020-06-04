# python
# The basic skill of open files
# There is the way to read files that identified path.
# 1. use 'sys' module to get operator dlls to get identified path.
# 2. sys.argv[0] is your programm, and argv[1] is the path.
# 3. use 'os' and 'glob' module to read multi-files.

import os
import sys
import glob

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
        

def readfile(infile):
    with open(infile, 'r') as fr:
        i =1
        j =1
        for raw in fr:            
            # print ("Read {} .....send it to anlyist!\n".format(raw.strip()))
            if i ==1:
                i=i+1
                print ("Read Title: \n {}\n".format(raw.strip()))
                continue
            i=i+1
            display(raw)
        print ("Total read {} lines.".format(i))
        print ("Total misanalised is {} lines.".format(j))

inputPath = sys.argv[1]
inputName = sys.argv[2]
file_lists = glob.glob(os.path.join(inputPath,inputName))
print ("# Output #3: The file reader! {}\n\t".format(file_lists))
for infile in file_lists:
    print ("Found {}, and send to read this file.\n\t".format(infile))
    readfile(infile)
