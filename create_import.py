import os
import subprocess

os.chdir('epicenter')
branches = subprocess.check_output(['git', 'branch', '-a'])
branches = branches.split()
commands = "git lfs migrate import --include=\"*.jar\""
for branch in branches:
    print("branch", branch)
    if b'remotes/' in  branch or b'master' in branch or b'*' in branch:
        break
    commands += " --include-ref=" + branch.decode('utf-8') 
print("command", commands)
os.system(commands)