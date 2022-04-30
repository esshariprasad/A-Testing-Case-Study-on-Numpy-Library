# 3- the number and location of the debug and assert statements in production files.
import os

import re
Total_asserts=0
current="NA"
Total_debug_statements=0
removefile="rm assertndebug.txt"

assert_lineno_str=""
debug_lineno_str=""
command='grep -r --include="*.py" --include="*.c"  --include="*.pyi" -n -E  "( {3,}assert\w*)|(DEBUG_ASSERT\(.*\))|DebugPrint|(\.debug\()" >> assertndebug.txt --exclude=assert_statement_agreegation.py --exclude=assertndebug.py --exclude=assertndebug-json.py --exclude="*test*.py" --exclude-dir={test,tests,testing,venv} '

os.system(removefile)                       

os.system(command)
Total_asserts_in_all_files=0
Total_debug_statements_in_all_files=0
file=open("./assertndebug.txt")
output= open("assert_debug_outputfile.csv", "w")
output.write('Location,Assertlineno,Debuglineno,AssertCount,DebugCount\n')

TotalTestFiles=0
for f in file:
    
    file_detail =f.split(":")
    file_name=file_detail[0]
    line_no=file_detail[1]
    line=file_detail[2]
    
    
    if(current==file_name):
        if(re.search("assert",line)):
            Total_asserts+=1
            Total_asserts_in_all_files+=1
            assert_lineno_str=assert_lineno_str+" "+line_no
        elif(re.search("debug",line,re.IGNORECASE)):
            Total_debug_statements+=1  
            Total_debug_statements_in_all_files+=1 
            debug_lineno_str=debug_lineno_str+" "+ line_no

    elif(current!=file_name):
        #first time see the file resert total asserts for file
        #set asserts=1
        TotalTestFiles+=1
        if(Total_asserts>0 or Total_debug_statements>0):
            
            output.write("\""+assert_lineno_str+"\""+",")
            output.write("\""+debug_lineno_str+"\"")
            assert_lineno_str=""
            debug_lineno_str=""

            output.write(","+str(Total_asserts))
            output.write(","+str(Total_debug_statements)+"\n")
       #assert and debug statement check
       #first time file is seen
        Total_asserts=0
        Total_debug_statements=0
        output.write(file_name+",")
        
        current=file_name
        
        if(re.search("assert",line)):
            Total_asserts=1
            Total_asserts_in_all_files+=1
            assert_lineno_str=""+line_no
        elif(re.search("debug",line)):
            Total_debug_statements=1   
            Total_debug_statements_in_all_files+=1 
            debug_lineno_str=""+line_no 
            # print(Total_debug_statements_in_all_files)

        
        #print new file_name
        
       
        

output.write("\""+assert_lineno_str+"\""+",")
output.write("\""+debug_lineno_str+"\"")    
output.write(","+str(Total_asserts))
output.write(","+str(Total_debug_statements)+"\n")


print("\n" +"TotalFiles with debug and assert statements: "+str(TotalTestFiles)+"\n")    
print("\n" +"Debug statements in total in all files: "+str(Total_debug_statements_in_all_files)+"\n")    
print("\n" +"Asserts statements in total in all files: "+str(Total_asserts_in_all_files)+"\n")  
file.close()        
       




    

       
        
        
