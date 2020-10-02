file = open("using-python-to-interact-with-the-operating-system/week-two/spider.txt")


print(file.readline())
print(file.readline())
print(file.read())

file.close()
with open("using-python-to-interact-with-the-operating-system/week-two/spider.txt") as file:
    print(file.readline())

    for line in file:
        print(line.upper())
        print(line.strip().upper())

file = open("using-python-to-interact-with-the-operating-system/week-two/spider.txt")
lines = file.readlines()
file.close
lines.sort()
print(lines)

    file.write("It was a dark and stormy night")



import os
os.remove("using-python-to-interact-with-the-operating-system/week-two/novel.txt")

os.rename("using-python-to-interact-with-the-operating-system/week-two/spider.txt", "using-python-to-interact-with-the-operating-system/week-two/spider_rename.txt")
os.rename("using-python-to-interact-with-the-operating-system/week-two/spider_rename.txt", "using-python-to-interact-with-the-operating-system/week-two/spider.txt")

print(os.path.exists("using-python-to-interact-with-the-operating-system/week-two/spider_rename.txt"))

print(os.path.getsize("using-python-to-interact-with-the-operating-system/week-two/spider.txt"))

print(os.path.getmtime("using-python-to-interact-with-the-operating-system/week-two/spider.txt"))

import datetime
timestap = os.path.getmtime("using-python-to-interact-with-the-operating-system/week-two/spider.txt")
print(datetime.datetime.fromtimestamp(timestap))
print(os.path.abspath("spider.txt"))
print(os.getcwd())
os.mkdir("using-python-to-interact-with-the-operating-system/week-two/new_dir")
os.chdir("using-python-to-interact-with-the-operating-system/week-two/new_dir")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.rmdir(os.path.abspath("new_dir"))
os.chdir("..")
print(os.getcwd())
print(os.listdir("week-two"))
dir = "week-two"
os.mkdir("week-two/another_new_dir")
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

os.rmdir("week-two/another_new_dir")

import csv
f = open("week-two/csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()

with open ("week-two/software.csv") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print("{} has {} users".format(row["name"], row["users"]))

users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
{"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
{"name": "Charlie Grey", "username": "greyc", "department": "Development" }]

keys = ["name", "username", "department"]

with open("week-two/by_department.csv", "w") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

os.remove("week-two/by_department.csv")
