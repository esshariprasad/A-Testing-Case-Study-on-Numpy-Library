# 3- the number and location of the debug and assert statements in production files.
import os

import re
Total_asserts=0
current="NA"
Total_debug_statements=0
removefile="rm assertndebug.txt"
# command='grep -r --include="*.py"  -n "   assert\|assert_[A-Za-z](\|.assert\|debug(" * >>assertndebug.txt --exclude=assert_statement_agreegation.py --exclude=assertndebug.py --exclude=assertndebug-json.py --exclude-dir=tests/*'
#command='grep -r --include="*.py"  -n "   assert\|assert_[A-Za-z](\|.assert\|debug(" * >>assertndebug.txt --exclude=assert_statement_agreegation.py --exclude=assertndebug.py --exclude=assertndebug-json.py --exclude-dir=tests/*'
command='grep -r --include="*.py" --include="*.c"  --include="*.pyi" -n -E  "( {3,}assert_\w*\(.*\))|( {3,}assert_\w{1,}_\w{1,}\(.*\))|( {3,}assert_\w{1,}_\w{1,}\(.*)|(.{3,}assert [A-Za-z]*.*\()|(DEBUG_ASSERT\()|(\.debug\()" >> assertndebug.txt --exclude=assert_statement_agreegation.py --exclude=assertndebug.py --exclude=assertndebug-json.py --exclude-dir={test,tests,testing}'
command='grep -r --include="*.py" --include="*.c"  --include="*.pyi" -n -E  "( {3,}assert\w*)|(DEBUG_ASSERT\()|(\.debug\()" >> assertndebug.txt --exclude=assert_statement_agreegation.py --exclude=assertndebug.py --exclude=assertndebug-json.py --exclude="*test*.py" --exclude-dir={test,tests,testing} '

os.system(removefile)
os.system(command)
Total_asserts_in_all_files=0
Total_debug_statements_in_all_files=0
file=open("./assertndebug.txt")
output= open("assert_debug_outputfile.txt", "w")
output.write("File to show the of the number of assert and debug statements in each Test file \n")
output.write("========================================================================================== \n")

output.write("\n")

output.write("\n")

output.write("Filename, \t Linenumber:Line_containing_assert_statement and debug statements \t Total asserts and debug statements for that file \n")
TotalTestFiles=0
for f in file:
    
    file_detail =f.split(":")
    file_name=file_detail[0]
    line_no=file_detail[1]
    line=file_detail[2]
    
    
    # print(file_name)
    # print(line)
    # print(line_no)
    if(current==file_name):
        ##saw file already
        #print lin_no and line
       

        output.write("\n")
        output.write(str(line_no)+": "+line)
        if(re.search("assert",line)):
            Total_asserts+=1
            Total_asserts_in_all_files+=1
        elif(re.search("debug",line)):
            Total_debug_statements+=1  
            Total_debug_statements_in_all_files+=1  

    elif(current!=file_name):
        #first time see the file resert total asserts for file
        #set asserts=1
        TotalTestFiles+=1
        if(Total_asserts>0 or Total_debug_statements>0):
            output.write("\n" +"Total asserts: "+str(Total_asserts)+"\n")
            output.write("\n" +"Total Debug statements: "+str(Total_debug_statements)+"\n")
       #assert and debug statement check
        Total_asserts=0
        Total_debug_statements=0
        if(re.search("assert",line)):
            Total_asserts=1
            Total_asserts_in_all_files+=1
        elif(re.search("debug",line)):
            Total_debug_statements=1   
            Total_debug_statements_in_all_files+=1  
            # print(Total_debug_statements_in_all_files)

        current=file_name
        #print new file_name
        output.write("\n"+"Filename: "+file_name+"\n")
        output.write(str(line_no)+": "+line)
    
output.write("\n" +"Total asserts: "+str(Total_asserts)+"\n")
output.write("\n" +"Total Debug: "+str(Total_debug_statements)+"\n")
output.write("\n" +"TotalFiles with debug and assert statements: "+str(TotalTestFiles)+"\n")    
output.write("\n" +"Debug statements in total in all files: "+str(Total_debug_statements_in_all_files)+"\n")    
output.write("\n" +"Asserts statements in total in all files: "+str(Total_asserts_in_all_files)+"\n")  
file.close()        
       




    

       
        
        
