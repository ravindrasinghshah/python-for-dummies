course_name = "Python Programming"
print((course_name.upper()))
print((course_name[0]))  # Get first char of string
print((course_name[-1]))  # Get last char of string
print((course_name[0:3]))  # Get 0-3 index values
print((course_name[0:]))  # Get full string
print((course_name[:3]))  # Get by default from 0 index
print((course_name[:]))  # Get full string
print((course_name.lower().find("pro")))  # Get index of char
print("Pro" in course_name)  # Bool check if char exists
print((course_name.replace("P", "R")))  # Replace matching chars

# Formatted string
first = "Ravindra"
middle = "Singh"
last = "Shah"
full = f"{first} {middle} {last}"
print(full)


# single line assignment

a, b = "ravi", "singh"
print(a, b)
