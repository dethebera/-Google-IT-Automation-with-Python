data = input("This comes from STDIN: ")
print("We are writing it to STDOUT: " + data)

import os

print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

import sys
print(sys.argv)

import os
import subprocess

print(subprocess.run(["date"]))
print(subprocess.run(["sleep", "2"]))
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)

print(result.stdout)
print(result.stdout.decode().split())

result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)


my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])
result = subprocess.run(["myapp"], env=my_env)


import re

logfile = sys.argv[1]
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            # continue keyword tells the loop to go to the next element
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        print(result)
