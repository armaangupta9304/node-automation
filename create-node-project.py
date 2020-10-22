import os
import sys
from project import NodeProjectMaker
options = []


try:
    for option in sys.argv:
        print(option)
        options.append(option)
    del options[0]
except:
    err = OSError("Bruh, Something Went Wrong!")

name = options[0]
additional = None
isMongoose = False

try:
    additional = options[1]
except:
    additional = None

try:
    if options[2] == 'True':
        isMongoose = True
except:
    isMongoose = False

print(additional)
project = NodeProjectMaker(options[0], os.getcwd(), additional=additional, isMongoose=isMongoose)
project.makeProject()