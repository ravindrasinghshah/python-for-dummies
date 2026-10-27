count = 0
for x in range(1, 10):
    if x % 2 == 0:
        print(x)
        count += 1
print(f"We have {count} even numbers")


# Another approach using third param in range
count = 0
for x in range(2, 10, 2):
    print(x)
    count += 1
print(f"We have {count} even numbers")
