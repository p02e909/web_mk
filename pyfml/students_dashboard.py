#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Do statistics on students' Merge Requests for given class_id
# TODO: get MR detail, check build result and get list of correct exercises
# Turn to a website, allow students login using GitLab ID
# Or turn to public site, use Lambda generates beautiful dashboard?
# Data can exported as JSON or CSV
"""
import argparse
import os
import datetime
from collections import namedtuple

import requests

argp = argparse.ArgumentParser(__doc__)
argp.add_argument('class_id', help='E.g pymihcm1804', type=str)

args = argp.parse_args()
class_id = args.class_id

Student = namedtuple('Student', ['gitlabid', 'name', 'openMR', 'closeMR'])

gitlab_time_format = '%Y-%m-%dT%H:%M:%S.%fZ'
start_2018 = datetime.datetime(2018, 1, 1)
start_2018_str = datetime.datetime.strftime(start_2018, gitlab_time_format)

token = open(os.path.expanduser('~/.config/gitlab')).read().strip()
headers = {'Private-Token': token}
base_url = 'https://gitlab.com/api/v4/'
group_members = base_url + 'groups/{}/members'

resp = requests.get(
    group_members.format(class_id),
    headers=headers,
    data={'per_page': 100}
)
resp_data = resp.json()

cntr = 1
students = []
print("List of {} students".format(class_id))
for student in resp_data:
    if isinstance(student, str):
        print(student, resp_data)
        continue
    if student['access_level'] < 50:
        s = Student(student['username'], student['name'], 0, 0)
        print(cntr, s)
        students.append(s)
        cntr += 1

# resp = requests.get('https://gitlab.com/api/v4/projects/pyfml%2Fpyfml',
#                    headers=headers)
# resp_data = resp.json()
# the URL get from above resp
MR_URL = 'https://gitlab.com/api/v4/projects/1591562/merge_requests'

merge_requests = []
page = 1
while True:
    print('Processing MRs page {}'.format(page))
    resp = requests.get(
        MR_URL,
        headers=headers,
        data={'per_page': 100, 'page': page, 'created_after': start_2018_str}
    ).json()
    if not resp:
        break
    merge_requests.extend(resp)
    page = page + 1
print(len(merge_requests))

counter = {s.gitlabid: {'openMR': 0, 'closeMR': 0, 'totalMR': 0}
           for s in students
           }

gitlabids = [s.gitlabid for s in students]

for mr in merge_requests:
    mr_author = mr['author']['username']
    if mr_author not in gitlabids:
        continue

    if mr['state'] == 'opened':
        counter[mr_author]['openMR'] += 1
    else:
        counter[mr_author]['closeMR'] += 1
    print(mr_author, mr['created_at'], '#{}'.format(mr['iid']), mr['state'])


sd = {s.gitlabid: s.name for s in students}

fmt = '{:<20} {:<10} {:<10} - {}'
print(fmt.format('GitLabID', 'openMRs', 'closeMRs', 'Name'))
for glid, mr_count in sorted(
        counter.items(), key=lambda x: x[1]['openMR'], reverse=True):
    print(fmt.format(glid, mr_count['openMR'], mr_count['closeMR'], sd[glid]))
