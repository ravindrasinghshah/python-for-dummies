for number in range(5):  # print numbers in range - by default range starts from 0
    print("Attempting to connect -", number + 1, (number + 1) * ".")

print(30 * "-")

for number in range(1, 5):  # print numbers in range
    print("Sending message -", number, number * ".")

print(30 * "-")

for number in range(1, 10, 2):  # print every second number in range
    print("Message sent -", number, number * ".")

for number in range(1, 20, 3):  # print every third number in range
    print("Message sent -", number, number * ".")

print(30 * "-")

success = True
for number in range(3):  # print numbers in range
    print("Attempt -", number + 1)
    if success:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

print(30 * "-")

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

print(30 * "-")

# Iterable
for x in "Python":
    print(x)

print(30 * "-")

for x in [1, 2, 3, 4, 5]:
    print(x)


print("For loop with index", 30 * "-")

for i, c in enumerate("PythonProgramming"):
    print(i, c)

print("For loop with index and str length", 30 * "-")
str = "Python Programming"
n = len(str)
for x in range(n):
    print(x, str[x])

print("While loop", 30 * "-")

number = 100
while number > 0:
    print(number)
    number //= 2

command = ""

while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
