import os
import subprocess

os.chdir('epicenter')
branches = subprocess.check_output(['git', 'branch', '-a'])
branches = branches.split()

for branch in branches:
    new_name = branch.split(b'branches/')
    print(new_name)
    if len(new_name) > 1:
        command = "git checkout -b " + new_name[1].decode('utf-8') + " " + branch.decode('utf-8')
        print(command) 
        os.system(command)