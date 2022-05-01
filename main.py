
from assertndebug import *
from assert_statement_agreegation import *
from CustomFiles.gen_data import *
import subprocess
import time


if __name__=="__main__":
    cmd0 = 'rm -rf csv_data'
    cmd1 = 'mkdir csv_data'
    rem_fig='rm -rf figures'
    fig_dir='mkdir figures'
    os.system(cmd0)
    os.system(cmd1)
    Generate_assertndebugCSV()
    Generate_assert_aggreagationCSV()
    time.sleep(5)

    p=subprocess.run(['python', './CustomFiles/gen_data_pre.py'])
    # p.kill()
    PydillerCSV()
    os.system(rem_fig)
    os.system(fig_dir)
    subprocess.run(['python', './CustomFiles/gen-figure.py'])

    
