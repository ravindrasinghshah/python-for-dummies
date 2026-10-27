def greet(first_name: str, last_name: str) -> None:
    print("Hi", first_name, last_name)
    print("Welcome abroad")


greet("Rob", "Smith")


def get_greet(first_name: any) -> str:
    return f"Hi, {first_name}"


print(get_greet("Batman"))
print(get_greet(420))


def increment(number: int, by: int = 1) -> int:
    return number + by


print(increment(by=2, number=1))  # can give keywords arguments in any order
print(increment(number=1))


def multiply(*numbers) -> float:
    total = 1
    for number in numbers:
        total *= number
    return total


print("Total:", multiply(2, 3, 4, 5))
