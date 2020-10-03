log = "July 31 7:51:48 mycomputer bad_process[12345]: ERROR Perfroming package upgrade"
index = log.index('[')

print(log[index+1:index+6])

import re
log = "July 31 7:51:48 mycomputer bad_process[12345]: ERROR Perfroming package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

result = re.search(r'aza', 'plaza')
print(result)

result = re.search(r'aza', 'bazaar')
print(result)

result = re.search(r'aza', 'maze')
print(result)

print(re.search(r"^x", "xenon"))
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "sponge"))

print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like dogs."))

print(re.findall(r"cat|dog", "I like both cats and dogs."))

print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py.*n", "Pyn"))

print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))

print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))

print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))

pattern = r"^[a-zA-Z0-9_]*$"
print(re.search(pattern, "this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable name"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)

print(result[0])
print(result[1])
print(result[2])
print("{} {}".format(result[2], result[1]))

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return print(name)
    return print("{} {}".format(result[2], result[1]))

rearrange_name("Lovelace, Ada")
rearrange_name("Ritchie, Dennis")
rearrange_name("Hopper, Grace M.")

def rearrange_name_updated(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
        return print(name)
    return print("{} {}".format(result[2], result[1]))

rearrange_name_updated("Hopper, Grace M.")


print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))

print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))
print(re.findall(r"\w{5,10}", "I really like strawberries"))
print(re.search(r"s\w{,20}", "I really like strawberries"))

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)]"
result = re.search(regex, log)
print(result[1])

result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])

def extract_pid(log_line):
    regex = r"\[(\d+)]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]

print(extract_pid(log))
print(extract_pid("99 elephants in a [cage]"))

print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))

print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))
