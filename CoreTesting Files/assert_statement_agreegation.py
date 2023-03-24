# 2- the number for test files and the number of assert statements in each file
import os
import re

def Generate_assert_aggreagationCSV():
    Total_asserts=0
    current="NA"
    Allasserts=0
    removefile="rm assertstatement.txt"

    command='grep -r --include="test*.py" --include="test*.c"  --include="*.pyi" -n -E  "( {3,}assert_\w*\(.*\))|( {3,}assert_\w{1,}_\w{1,}\(.*\))|( {3,}assert_\w{1,}_\w{1,}\(.*)|(.{3,}assert [A-Za-z]*.*\()|( {3,}assert * [A-Za-z]+\.[A-Za-z_]*)|(assert.*==)|(assert.*!=)|(assert.*[><][A-Za-z0-9])|(assert.* is .*)|(assert\(.*;)" >>assertstatement.txt --exclude=assert_statement_agreegation.py --exclude=assertndebug.py --exclude="pydiller.py" --exclude=main.py'

    os.system(removefile)
    os.system(command)

    file=open("./assertstatement.txt")
    output= open("./csv_data/assertstatement_aggreegation.csv", "w")
    # output.write("File to show the of test files and the number of assert statements in each Test file \n")
    # output.write("========================================================================================== \n")
    output.write('Location,Assertlineno,AssertCount\n')

    # output.write("Filename, \t Linenumber:Line_containing_assert_statement \t Total asserts for that file \n")
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
            
            # output.write("\n")
            # output.write(str(line_no)+": "+line)
            output.write(" "+str(line_no))
            Total_asserts+=1
            Allasserts+=1

        elif(current!=file_name):
            #first time see the file resert total asserts for file
            #set asserts=1
            TotalTestFiles+=1
            Allasserts+=1
            if(Total_asserts>0):
                output.write("\""+",")
                output.write(str(Total_asserts)+"\n")
            Total_asserts=1
            current=file_name
            #print new file_name
            output.write(file_name)
            # name=file_name.split("/")
            # print(name)
            # output.write(file_name)
            # output.write(","+name)
            output.write(","+"\"")
            output.write(" "+str(line_no))
            # output.write(str(line_no)+": "+line)

    # print(Total_asserts)
    print(Allasserts)
    output.write("\""+","+str(Total_asserts))

    print("\n" +"Total Test Files: "+str(TotalTestFiles)+"\n")    

    file.close()        
        




        

        
            
            
