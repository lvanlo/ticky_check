#!/usr/bin/env python3
import re
import operator
import sys
import csv

#dict: number of different errors
errors = {}
#dict: number of entries per user
users = {}

#Open and read files and create dictionaries
with open('syslog.log') as file:
  for line in file.readlines():
    error_string = 'ERROR'
    info_string = 'INFO'
    error = re.fullmatch(
      r"ticky: ([\w+]*):? ([\w' ]*)[\[[0-9]*\]?]? ?\((.*)\)$", error_string)
    info = re.fullmatch(
      r"ticky: ([\w+]*):? ([\w' ]*)[\[[0-9]*\]?]? ?\((.*)\)$", info_string)
    user = re.search(r" ?\((.*)\)", line)

  if error not in errors.keys():
    errors[error] = 1
  else:
    errors[error] += 1

  #checks if user is in info or error
  if user not in users.keys() or user not in errors.keys():
    users[user] = {}
    users[user][error] = 0
    users[user][info] = 0
    if info not in users.keys():
      users[user] = {}
      users[user][info] = 0
    else:
      user[info] += 1
    if error not in user.keys():
      users[user] = {}
      users[user][error] = 0
    else:
      users[error] += 1

#sorted by
errors_list = sorted(errors.items(), key=operator.itemgettergetter(1), reverse=True)
user_list = sorted(users.items(), key=operator.itemgetter(0))

file.close()

#Insert at the beginning of the list
errors_list.insert(0, ('Error', 'Count'))

# * Create CSV file user statistics
with open('user_statistics.csv', 'w', newline='') as user_csv:
  for key, value in user_list:
    user_csv.write(str(key) + ',' + str(value[info]) + ',' + str(value[error])+'\n')

with open('error_message.csv', 'w', newline='') as error_csv:
  for key, value in errors_list:
    error_csv.write(str(key) + ' ' + str(value))
