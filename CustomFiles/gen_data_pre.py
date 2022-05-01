
from datetime import datetime
from pydriller import Repository
from ast import Assert
import pandas as pd
import os

dir_store=os.getcwd()
dir_store=dir_store+"/csv_data/"
data=pd.read_csv(dir_store+"assertstatement_aggreegation.csv")
all=[]
series = data["AssertCount"]
File_Locations = data["Location"]
for f in range(len(File_Locations)):
    folder_name=File_Locations[f]
    folder_name=folder_name.split("/")[2]
    all.append(folder_name)

data['outer_location'] =all    
data_grouped=data.groupby('outer_location').sum()
data_grouped.to_csv(dir_store+"assertCountOnFolderLevel.csv")



data=pd.read_csv(dir_store+"assert_debug_outputfile.csv")
all=[]

series = data["AssertCount"]
File_Locations = data["Location"]
for f in range(len(File_Locations)):
    folder_name=File_Locations[f]
    folder_name=folder_name.split("/")[-2]
    
    all.append(folder_name)

data['outer_location'] =all    
data_grouped=data.groupby('outer_location').sum()

data_grouped.to_csv(dir_store+"Folder_Assert_Debug_Count.csv")


