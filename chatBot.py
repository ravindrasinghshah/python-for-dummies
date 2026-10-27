bot_name: str = "Bob"
print(f"Hello I'm {bot_name}! How can I assist you today?")


while True:
    user_input: str = input("You: ").lower()

    if user_input in ["hi", "hello"]:
        print(f"{bot_name}: Hi there! How can I help you?")
    if user_input in ["bye", "see you"]:
        print("Goodbye!")
        break
    else:
        print("Please try again!")
