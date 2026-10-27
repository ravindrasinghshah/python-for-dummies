a, b = 10, "fifteen"

try:
    print(a + b)
except Exception as e:
    print(f"Something went wrong: {e}")
    print(f"Please enter a number")

print("Continuing with program")
