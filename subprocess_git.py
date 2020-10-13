import subprocess

commit_message = "subprocess_git.py"
# this works
# subprocess.call(["git", "status"])
subprocess.call(["git", "add", "-A"])
subprocess.call(["git", "commit", "-m", commit_message])
subprocess.call(["git", "push"])