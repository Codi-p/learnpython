# python
# The basic skill of open files
# There is the way to read files that identified path.
# 1. use 'sys' module to get operator dlls to get identified path.
# 2. sys.argv[0] is your programm, and argv[1] is the path.
# 3. use 'os' and 'glob' module to read multi-files.

import os
import sys
import glob

inputPath = sys.argv[1]
print ("# Output #3: The file reader! {}\n\t".format(glob.glob(os.path.join(inputPath, '*.py'))))
for infile in glob.glob(os.path.join(inputPath, '*.py')):
    print ("Found {}.\n\t".format(infile))
    with open(infile, 'r') as filereader:
        for row in filereader:
            print ("{}".format(row.strip()))
