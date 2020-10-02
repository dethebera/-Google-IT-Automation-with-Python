def double_word(word):
    word *= 2
    count = 0
    for letter in word:
        count += 1
    return word + str(count)

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

def first_and_last(message):
    if message == "" or message[0] == message[-1]:
        return True
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
word = "supercalifragilisticexpialidocious"
print(word.index("x"))

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS


def student_grade(name, grade):
    return "{name} received {grade}% on the exam".format(name=name, grade=grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))


def group_list(group, users):
    members = group + ": " + ", ".join(users)
    return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"


def skip_elements(elements):
    new_elements = []
    for element in elements:
        if elements.index(element) % 2 == 0:
            new_elements.append(element)
    return new_elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []


The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out:
Ken is 30 years old and works as Chef.
Pat is 35 years old and works as Lawyer.
Amanda is 25 years old and works as Engineer.
Fill in the gaps in this function to do that.
"""
def guest_list(guests):
	for guest in guests:
		name, age, job = guest
		print("{} is {} years old and works as {}".format(name, age, job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])


def skip_elements_enumerate(elements):
	new_elements = []
	for index, element in enumerate(elements):
	  if(index % 2 == 0):
	    new_elements.append(element)
	return new_elements

print(skip_elements_enumerate(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements_enumerate(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


def skip_elements_list_comprehension(elements):
	return [element for element in elements if elements.index(element) % 2 == 0]  

print(skip_elements_list_comprehension(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements_list_comprehension(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents?
print("Chapter 5" in toc) # Is there a Chapter 5?


cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for beast, feature in cool_beasts.items():
    print("{} have {}".format(beast, feature))


wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for cloth in wardrobe:
    for color in wardrobe[cloth]:
        print("{} {}".format(color, cloth))
