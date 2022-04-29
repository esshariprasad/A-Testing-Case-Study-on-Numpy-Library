import csv
from pydriller import Repository
import sys
import collections

sys.setrecursionlimit(1000000)
testfiles_authordate = {}
testfiles_authorsinvolved = {}
testfiles_modificationfrequency = {}
directories = ['test', 'unittests']


def getTestFilesWithDateAuthorsAndModificationFrequency():
  for commit in Repository('https://github.com/llvm-mirror/llvm', from_commit=
  '8d0afd3d32d1d67f9aa5df250a1d6955aa8f1ac9', to_commit='a52f3ae45ce28198bb402ddea8db5a8cb8d8ced7').traverse_commits():

    for file in commit.modified_files:
      if checkDirectory(file.new_path):
        if not testfiles_authordate.keys().__contains__(file.filename):
          testfiles_authordate[file.filename] = commit.author_date

        if testfiles_authorsinvolved.get(file.filename) is not None:
          testfiles_authorsinvolved.get(file.filename).add(commit.author.name)
        else:
          testfiles_authorsinvolved[file.filename] = {commit.author.name}

        if testfiles_modificationfrequency.get(file.filename) is not None:
          testfiles_modificationfrequency.get(file.filename).add(commit.author_date)
        else:
          testfiles_modificationfrequency[file.filename] = {commit.author_date}


def checkDirectory(file_path):
  return any(element in file_path for element in directories) if file_path is not None else False


getTestFilesWithDateAuthorsAndModificationFrequency()
testfiles_authordate = collections.OrderedDict(sorted(testfiles_authordate.items()))
print(testfiles_authordate)
testfiles_authorsinvolved = collections.OrderedDict(sorted(testfiles_authorsinvolved.items()))
print(testfiles_authorsinvolved)
testfiles_modificationfrequency = collections.OrderedDict(sorted(testfiles_modificationfrequency.items()))
print(testfiles_modificationfrequency)


def checkForFile(file_name):
  return testfiles_authordate.__contains__(file_name) and testfiles_authorsinvolved.__contains__(
    file_name) and testfiles_modificationfrequency.__contains__(filename)


def transformDateFormat(dates_set):
  modified_dates = ''
  for temp_date in dates_set:
    modified_dates = modified_dates + '  ' + temp_date.date().strftime("%Y-%m-%d")

  return modified_dates


with open('files.csv', 'w', newline='') as file_object:
  headerCSV = ['FileName', 'DateWhenFileIsAddedToTheProject', 'NumberOfAuthorsInvolved', 'ModificationDates']
  writer = csv.DictWriter(file_object, fieldnames=headerCSV)
  writer.writeheader()
  for filename in testfiles_authorsinvolved.keys():
    if checkForFile(filename):
      dates_modified = transformDateFormat(testfiles_modificationfrequency[filename])
      file_object.write("%s, %s, %d, %s\n" % (filename, testfiles_authordate[filename].date(),
                                              len(testfiles_authorsinvolved[filename]),
                                              dates_modified))
  file_object.close()
