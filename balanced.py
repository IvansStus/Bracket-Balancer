# Ivan Stus CS320
# Lab 1 - balanced.py

import sys  #Import used to read comman line prompt
import os   #Import os used to split file from the extension

#Opening file that was input in cmd prompt
with open(sys.argv[1], 'r') as input_File:
    input_File_Contents = open(sys.argv[1]).readlines()     #read every line of the input file  

#Opening output file with .nocom to strip the file of comments
with open((os.path.splitext(sys.argv[1])[0]+'.nocom'), 'w') as output_File:
    nestedcomment = False   #Nested comment multi line check
    for line in input_File_Contents:    #loop thru line by line
        if "/*" and "*/" in line:   #test for nested comment in line          
            data = line.split("/*")     
            data2 = line.split("*/")        
            line = data[0] + data2[1]   #set line to before 1st split and after 2nd split
        if "/*" in line:        #checks for beginning of nested comment
            nestedcomment = True
            data = line.split("/*")
            line = data[0]      #discards everything after /*
        elif "*/" in line and nestedcomment:
            nestedcomment = False
            data = line.split("*/") 
            line = data[1]      #discards everything before */
        elif nestedcomment:
            line = None     #discards everything in between /* & */
        else:   #checks and separates end of the line single comments
            if '/' in line:
                sep = '/'
                line = line.split(sep)[0]
            output_File.writelines(line + '\n')     #writes lines of input file to output file, comment-free

#Re-open file to read the lines for balancing        
with open((os.path.splitext(sys.argv[1])[0]+'.nocom'), 'r') as print_File:    
    open_list = ["[","{","("]   #array to check for open chars
    close_list = ["]","}",")"]  #array to check for closing chars
    stack = []    
    for line in print_File:
        in_quotation = False    #checks to see if there are any "", if there are, then continue without adding to stack
        for chars in line:
            if in_quotation and chars != "\"":
                continue
            elif in_quotation and chars == "\"":
                in_quotation = False
                continue
            else:
                if chars == "\"":
                    in_quotation = True
                if chars in open_list: 
                    stack.append(chars)     #add char to stack if it is in opening char array                                    
                elif chars in close_list: 
                    pos = close_list.index(chars) 
                    if ((len(stack) > 0) and       #checks if end of open list = end of close list
                        (open_list[pos] == stack[len(stack)-1])): 
                        stack.pop()     #pop array if closing char matches stack                         
                    else:
                        print("Unbalanced")     
                        exit()
    if len(stack) > 0:  #double checks to see if length of the stack is greater than 0
        print("Unbalanced")
        exit()          
    if len(stack) == 0: #if check is done and stack is empty, the file is balanced
        print("Balanced") 
        exit() 