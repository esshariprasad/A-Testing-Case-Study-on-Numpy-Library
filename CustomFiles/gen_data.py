import sys
import os
import csv
import operator
import itertools
import calendar
import collections
from datetime import datetime
from pydriller import Repository
from ast import Assert

dir_store=os.getcwd()
url = ["https://github.com/numpy/numpy.git"]

dict = {}
commit_msgs = []

dict_commit_msgs = {}

dict_author_count = {}
dict_month_count = {}
dict_year_count = {}

def PydillerCSV():
  

    # for commit in Repository(path_to_repo=url, since=datetime(2022, 3, 1, 17, 0, 0)).traverse_commits():
    for commit in Repository(path_to_repo=url).traverse_commits():
        for m in commit.modified_files:
            if(m.filename.startswith('test') and (m.filename.endswith('.py') or (m.filename.endswith('.c')))):
                if commit.author.name not in dict_author_count:
                    dict_author_count[commit.author.name] = 0
                dict_author_count[commit.author.name] += 1
                
                # full_month_name = calendar.month_name[commit.author_date.month]
                # if str(full_month_name) not in dict_month_count:
                #     dict_month_count[str(full_month_name)] = 0
                # dict_month_count[str(full_month_name)] += 1

                if commit.author_date.year not in dict_year_count:
                    dict_year_count[commit.author_date.year] = 0
                dict_year_count[commit.author_date.year] += 1

                if m.filename not in dict.keys():
                    dict[m.filename] = {}
                    dict[m.filename]['people_involved'] = []
                    dict[m.filename]['modified_date'] = []
                    dict[m.filename]['created_date'] = ""
                    dict[m.filename]['file_path'] = ""
                    dict[m.filename]['modified_count'] = 0

                if len(dict[m.filename]['modified_date']) == 0:
                    dict[m.filename]['created_date'] = commit.author_date

                if commit.author_date.date() not in dict[m.filename]['modified_date']:
                    dict[m.filename]['modified_date'].append(commit.author_date.date())
                dict[m.filename]['modified_count'] += 1
                # dict[m.filename]['file_path'] = m.new_path
                dict[m.filename]['file_path'] = m.new_path

                commit_msgs.append(commit.msg)

                if commit.author_date.year not in dict_commit_msgs:
                    dict_commit_msgs[commit.author_date.year] = []
                dict_commit_msgs[commit.author_date.year].append(commit.msg)

                if commit.author.name not in dict[m.filename]['people_involved']:
                    dict[m.filename]['people_involved'].append(commit.author.name)
    WriteToFiles()



def modified_dates(input):
    #print(type(input))
    modified_dates = ''
    for temp_date in input:
        modified_dates = modified_dates + ' ' + temp_date.strftime('%Y-%m-%d')

    return modified_dates

def people_involved(input):
    list = ''
    for i in input:
        list = list + ' ' + i
    return list


def total_fix_msgs(input):
    msgs_count = 0
    for i in input:
        if(i.lower().startswith('fix ')):
            msgs_count +=1
    return msgs_count

def total_bug_msgs(input):
    msgs_count = 0
    for i in input:
        if(i.lower().startswith('bug:')):
            msgs_count +=1
    return msgs_count

def WriteToFiles():
   
    file = open(dir_store+'/csv_data/all_data_pydriller.csv', 'w', newline='',encoding="utf-8")
    writer = csv.DictWriter(file, fieldnames=['File path','File Name', 'Test Files Added Date', 'Number Of People Involved', 'Number of Modifications','Modification Dates', 'People involved'])
    writer.writeheader()
    for k, v in dict.items():
        dates = modified_dates(dict[k]['modified_date'])
        #print('%s, %s, %s, %s\n' % (k,str(dict[k]['created_date'].date()), len(dict[k]['people_involved']), dates))
        file.write("%s, %s, %s, %d, %d, %s, %s\n" % (str(dict[k]['file_path']),str(k), str(dict[k]['created_date'].date()), len(dict[k]['people_involved']), dict[k]['modified_count'], dates, people_involved(dict[k]['people_involved'])))
    file.close()

    file = open(dir_store+'/csv_data/overview.csv', 'w', newline='',encoding="utf-8")
    writer = csv.DictWriter(file, fieldnames=['File Name', 'Test Files Added Date', 'Number Of People Involved', 'Number of Modifications'])
    writer.writeheader()
    for k, v in dict.items():
        file.write("%s, %s, %d, %d\n" % (str(k), str(dict[k]['created_date'].date()), len(dict[k]['people_involved']), dict[k]['modified_count']))
    file.close()

    # # sorted_dict_author_count = dict( sorted(dict_author_count.items(), key=operator.itemgetter(1),reverse=True))
    # # top_five_dict_author_count= dict(itertools.islice(sorted_dict_author_count.items(), 5)) 

    # top_five_contributors = open('top5contributors.csv', 'w', newline='',encoding="utf-8")
    # writer = csv.DictWriter(top_five_contributors, fieldnames=['Contributor', 'Commits'])
    # writer.writeheader()
    # for k, v in dict_author_count.items():
    #     if v > 100:
    #         top_five_contributors.write("%s, %d\n" % (str(k), v))
    # top_five_contributors.close()

    sorted_d = collections.OrderedDict(sorted(dict_author_count.items(), key=operator.itemgetter(1),reverse=True))

    top_five_contributors = open(dir_store+'/csv_data/top5contributors.csv', 'w', newline='')
    writer = csv.DictWriter(top_five_contributors, fieldnames=['Contributor', 'Commits'])
    writer.writeheader()
    # for val in dict_descending:
    #     top_five_contributors.write("%s, %d\n" % (str(val), dict_author_count.get(val)))
    top_five_count = 0
    # for k, v in dict_author_count.items():
    #     top_five_contributors.write("%s, %d\n" % (str(k), v))
    for k, v in sorted_d.items():
        if top_five_count <5:
            top_five_contributors.write("%s, %d\n" % (str(k), v))
        else:
            break
        top_five_count += 1
    top_five_contributors.close()



    # commits_month_wise = open('commits_month_wise.csv', 'w', newline='',encoding="utf-8")
    # writer = csv.DictWriter(commits_month_wise, fieldnames=['Month', 'Commits'])
    # writer.writeheader()
    # for k, v in dict_month_count.items():
    #     commits_month_wise.write("%s, %d\n" % (str(k), v))
    # commits_month_wise.close()

    commits_year_wise = open(dir_store+'/csv_data/commits_year_wise.csv', 'w', newline='',encoding="utf-8")
    writer = csv.DictWriter(commits_year_wise, fieldnames=['Year', 'Commits'])
    writer.writeheader()
    for k, v in dict_year_count.items():
        commits_year_wise.write("%d, %d\n" % (k, v))
    commits_year_wise.close()

    commit_fixes_year_wise = open(dir_store+'/csv_data/commit_fixes_year_wise.csv', 'w', newline='',encoding="utf-8")
    writer = csv.DictWriter(commit_fixes_year_wise, fieldnames = ['Year', 'Fixes'])
    writer.writeheader()
    for k, v in dict_commit_msgs.items():
        
        commit_fixes_year_wise.write("%d, %d\n" % (k, total_fix_msgs(v)))
    commit_fixes_year_wise.close()


    commit_bugs_year_wise = open(dir_store+'/csv_data/commit_bugs_year_wise.csv', 'w', newline='',encoding="utf-8")
    writer = csv.DictWriter(commit_bugs_year_wise, fieldnames = ['Year', 'Issues'])
    writer.writeheader()
    for k, v in dict_commit_msgs.items():    
        commit_bugs_year_wise.write("%d, %d\n" % (k, total_bug_msgs(v)))
    commit_bugs_year_wise.close()

    # fix_msgs_count = 0
    # bug_msgs_count = 0
    # for i in commit_msgs:
    #     if(i.lower().startswith('fix ')):
    #         fix_msgs_count +=1
    #     if(i.lower().startswith('bug:')):
    #         bug_msgs_count +=1
    # print("total fix msgs (count)", fix_msgs_count)
    # print("total bug msgs (count)", bug_msgs_count)
