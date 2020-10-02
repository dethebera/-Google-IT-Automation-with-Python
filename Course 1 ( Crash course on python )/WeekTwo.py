print(type("a"))
print(type(2))
print(type(2.5))

base = 5
height = 3
area = (base * height) / 2

print(area)


sum = 2048 + 4357 + 97658 + 125 + 8
amount = 5
average = sum/amount

print("The average size is: " + str(average))

def print_seconds(hours, minutes, seconds):
    print((hours * 60 * 60) + (minutes * 60) + seconds)

print_seconds(1,2,3)


def get_seconds(hours, minutes, seconds):
    return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

june_hours = 243
june_cost = june_hours * 0.65
print("In June we spent: " + str(june_cost))

july_hours = 325
july_cost = july_hours * 0.65
print("In July we spent: " + str(july_cost))

august_hours = 298
august_cost = august_hours * 0.65
print("In August we spent: " + str(august_cost))

def print_monthly_expense(month, hours):
    print("In " + month + " we spent: " + str(hours * 0.65))

print_monthly_expense("June", 243)
print_monthly_expense("July", 325)
print_monthly_expense("August", 298)

def f1(x, y):
	z = x*y  # the area is base*height
	print("The area is " + str(z))

def rectangle_area(base, height):
    area = base*height
    print("The area is " + str(area))

rectangle_area(5, 6)

print(10 > 1) # True
print("cat" == "dog") # False
print(1 != 2) # True
print(1 == "1") # False
print("Yellow" > "Cyan" and "Brown" > "Magenta") # False
print(25 > 50 or 1 != 2) # True
print(not 42 == "Answer") # True

def is_positive(number):
    if number > 0:
        return True

def is_positive_two(number):
    if number > 0:
        return True
    else:
        return False

def number_group(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative
