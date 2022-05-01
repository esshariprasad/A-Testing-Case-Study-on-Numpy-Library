import pandas as pd
# import matplotlib.pyplot as plt
import plotly.express as px
import plotly
import os

import plotly.graph_objects as go


dir_store=os.getcwd()

#3Q Assert
def Fig1():
    
    assertDebugCount = pd.read_csv(dir_store+"/csv_data/Folder_Assert_Debug_Count.csv")

    fig = px.bar(assertDebugCount,x=assertDebugCount["outer_location"], 
                    y = assertDebugCount["AssertCount"],
                    title="Count of Assert statements in each folder in Production",
                    labels={'outer_location' : 'Folder', 'AssertCount':'Count of Assert statements'}, 
                    text_auto=True, template="simple_white").update(layout=dict(title=dict(x=0.5)))

    fig.write_image(dir_store+"/figures/CountOfAssertStatementsInProduction.jpg")
    

# 3Q Debug
def Fig2():
    assertDebugCount = pd.read_csv(dir_store+"/csv_data/Folder_Assert_Debug_Count.csv")

    fig = px.bar(assertDebugCount,x=assertDebugCount["outer_location"], 
                    y = assertDebugCount["DebugCount"],
                    title="Count of Debug statements in each folder in Production",
                    labels={'outer_location' : 'Folder', 'DebugCount':'Count of Debug statements'}, 
                    text_auto=True, template="simple_white").update(layout=dict(title=dict(x=0.5)))

    fig.write_image(dir_store+"/figures/CountOfDebugStatementsInProduction.jpg")
    
#2Q:Asserts in Test file
def Fig3():
    assertCountOnFolderLevel = pd.read_csv(dir_store+"/csv_data/assertCountOnFolderLevel.csv")

    fig = px.bar(assertCountOnFolderLevel,x=assertCountOnFolderLevel["outer_location"], 
                    y = assertCountOnFolderLevel["AssertCount"],
                    title="Count of Assert statements in each folder",
                    labels={'outer_location' : 'Folder', 'AssertCount':'AssertCount'}, 
                    text_auto=True, template="simple_white").update(layout=dict(title=dict(x=0.5)))


    fig.write_image(dir_store+"/figures/CountOfAssertStatements.jpg")
    


# def Fig4():
#     testFilesCount = pd.read_csv(dir_store+"/csv_data/TestFilecount.csv")
#     testFilesCount.head


#     fig = px.bar(testFilesCount,x=testFilesCount["outer_location"], y = testFilesCount["Location"],
#                         title="Number of test files in each folder",
#                         labels={'outer_location' : 'Folder', 'Location':'Number of Test Files'}, 
#                         text_auto=True, template="simple_white").update(layout=dict(title=dict(x=0.5)))


#     fig.write_image(dir_store+"/figures/NumberOfTestFiles.jpg")
    
#Top 5 Contributers
def Fig5():

    topContributors = pd.read_csv(dir_store+"/csv_data/top5contributors.csv")
    topContributors.head

    top5 = topContributors.nlargest(5, 'Commits', keep='first')
    top5.head

    fig = px.bar(top5, x = top5["Contributor"], y = top5["Commits"],
                    title="Top Five Contributors",
                    labels={'Contributor' : 'Contributor', 'Commits':'Number of Commits'}, 
                    text_auto=True, template="simple_white").update(layout=dict(title=dict(x=0.5)))

    fig.write_image(dir_store+"/figures/TopFiveContributors.jpg")
    
#Issues over the years
def Fig6():

    commit_bugs_year_wise = pd.read_csv(dir_store+"/csv_data/commit_bugs_year_wise.csv")
    commit_bugs_year_wise.head

    fig = px.bar(commit_bugs_year_wise, x = commit_bugs_year_wise["Year"], y = commit_bugs_year_wise["Issues"],
                    title="Bug issues over years",
                    labels={'Year': 'Year', 'Issues':'Number of Commits'}, 
                    text_auto=True, template="simple_white").update(layout=dict(title=dict(x=0.5)))

    fig.write_image(dir_store+"/figures/BugIssuesOverYears.jpg")
    

#Commits over the years
def Fig7():
    commits_year_wise = pd.read_csv(dir_store+"/csv_data/commits_year_wise.csv")
    commits_year_wise.head

    fig = px.line(commits_year_wise, x="Year", y="Commits",
                title="Test Files over the years",
                labels={'Year': 'Year', 'Commits':'Number of Commits'}, template="simple_white").update(layout=dict(title=dict(x=0.5)))

    fig.write_image(dir_store+"/figures/CommitsOverYears.jpg")
    
#Fixes over the years
def Fig8():

    commit_fixes_year_wise = pd.read_csv(dir_store+"/csv_data/commit_fixes_year_wise.csv")
    commit_fixes_year_wise.head

    fig = px.bar(commit_fixes_year_wise, x = commit_fixes_year_wise["Year"], y = commit_fixes_year_wise["Fixes"],
                    title="Bug Fixes over years",
                    labels={'Year': 'Year', 'Fixes':'Number of Fixes'}, 
                    text_auto=True, template="simple_white").update(layout=dict(title=dict(x=0.5)))


    fig.write_image(dir_store+"/figures/BugFixesOverYears.jpg")

#4Q Table    
def overview_table():

    Datatable = pd.read_csv(dir_store+"/csv_data/overview.csv")
    Datatable = Datatable.nlargest(10, 'Number of Modifications', keep='first')
    headerColor = 'grey'
    rowEvenColor = 'lightgrey'
    rowOddColor = 'white'
    fig = go.Figure(data=[go.Table(
    header=dict(
    values=['<b>File Name</b>','<b>Test Files Added Date</b>','<b>Number Of People Involved</b>',
    '<b>Number of Modifications</b>'],
    line_color='darkslategray',
    fill_color=headerColor,
    align=['left','center'],
    font=dict(color='white', size=12)
    ),

    cells=dict(
    values=[Datatable["File Name"], Datatable["Test Files Added Date"],
    Datatable["Number Of People Involved"], Datatable["Number of Modifications"]],
    line_color='darkslategray',

    # 2-D list of colors for alternating rows
    fill_color = [[rowOddColor,rowEvenColor]*10],
    align = ['left', 'center'],
    font = dict(color = 'darkslategray', size = 11)
    ))
    ])
    fig.update_layout(title_text='Pydriller Sample Data Overview',title_x=0.5)
    fig.write_image(dir_store+"/figures/OverviewTable.jpg")
    


if __name__ == '__main__':
    # print("main")
    Fig1()
    Fig2()
    Fig3()
    # Fig4()
    Fig5()
    Fig6()
    Fig7()
    Fig8()
    overview_table()