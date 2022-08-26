'''
Some projects couldn't be scored by Scorecard and showed up as empty JSONs:

Apache: 3 missing
CNCF: 0 missing
Eclipse: 14 missing
Google: 19 missing
Huawei: 2 missing
IBM: 0 missing
Microsoft: 5 missing
Samsung: 9 missing
Tencent: 0 missing
'''

import os
import json

original_repos = []
empty_repos = []
to_write = []

directory = '/Users/jaco/Desktop/Coding/new_repos/New_CNCF/real_cncf'

for file in os.listdir(directory):
    # print(file)
    # print(os.stat(os.path.join(directory, file)).st_size)
    if os.stat(os.path.join(directory, file)).st_size == 0:

        github, sep, after = file.partition('.com')
        before, sep, after2 = after.partition('-')
        group, sep, bodyjson = after2.partition('-')
        body, sep, json = bodyjson.partition('.json')
        newurl = "github.com/" + group + "/" + body
        
        empty_repos.append(newurl)
# print("Empty repos:", empty_repos)
# print("Empty repo count:", len(empty_repos))

repo_counter = 0
for repo in empty_repos:
	repo = repo + '\n' 	
	to_write.append(repo)

with open('new_repos.txt', 'w') as t:
	for i in to_write:
		t.writelines(i)
