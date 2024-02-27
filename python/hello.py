# Ask user for their name
name = input("What's your name? ").strip().title()

# Split the name into first and last
first, last = name.split(" ")

# Say hello to the user
print(f"Hello, {first}!")
