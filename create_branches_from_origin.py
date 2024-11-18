import os
import subprocess

os.chdir('p4MigTest4')
branches = subprocess.check_output(['git', 'branch', '-a'])
branches = branches.split()
for branch in branches:
    new_name = branch.split(b'origin/')
    if len(new_name) > 1:
        command = "git checkout -b " + new_name[1].decode('utf-8') + " " + branch.decode('utf-8')
        print(command) 
        os.system(command)