# This function asks for the user's name and greets them.
name = input("What is your name? ").title()
clean = " ".join(name.split())
print(f"Hello, {clean}!")