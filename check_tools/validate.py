import mmap
import re
import os
import sys
from optparse import OptionParser

words = {}

def validate_file(inputfilename, compact=False):
    global words
    
    if not compact:
        print "Validating file:%s"%inputfilename
    input_file = open(inputfilename)
    alllines = input_file.readlines()
    
    line=1
    first = True
    for eachline in alllines:
        result = re.findall(words,eachline,flags=re.IGNORECASE)
        for eachresult in result:
            if eachresult!=None and len(eachresult)!=0:
                if compact:
                    if first:
                        sys.stdout.write(":%s:%d,%s" % (inputfilename, line, str(eachresult)))
                    else:
                        sys.stdout.write(";%d,%s" % (line, str(eachresult)))
                else:
                    print "\tLine %d:found \"%s\"" % (line, str(eachresult))
                first = False
        line=line+1            

def main():
    global words
    parser = OptionParser()
    parser.add_option("-f", "--inputfile",  dest="inputfile",  action="store", type="string", default="" , help="File to be validated", metavar="FILE")
    parser.add_option("-i", "--wordsfile", dest="wordsfile", action="store", type="string", default="prohibited.txt", help="File containing the words to be checked", metavar="FILE")
    parser.add_option("-c", "--compact", dest="compact", action="store_true", default=False, help="Format output text for human readability (verbose) or compact for scripting") 

    (options, args) = parser.parse_args()

    if len(options.inputfile) <= 0 or len(options.wordsfile) == None:
        parser.error("Invalid arguments")
        
    words_file = open(options.wordsfile)
    alllines = words_file.read()
    words = alllines[:-1].replace("\n","|")   
 
    if os.path.isfile(options.inputfile):
        validate_file(options.inputfile, options.compact)
        
    if(os.path.isdir(options.inputfile)):
        for root, dirs, files in os.walk(options.inputfile, topdown=False):
            for name in files:
                file_to_validate=os.path.join(root, name)
                if(file_to_validate.endswith(".md")):
                    validate_file(os.path.join(root, name), options.compact)  
            #   print(os.path.join(root, name))
            #for name in dirs:
            #   print(os.path.join(root, name)) 
      
if __name__ == "__main__":
    main() 
