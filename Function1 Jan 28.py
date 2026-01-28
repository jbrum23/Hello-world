# Greet the user by name, ensuring proper capitalization and removing extra spaces

def hello(to):
    print("Hello," , to)

# output greeting
name = input("What is your name? ")
hello(name)

# Output without passing the expected arguments
hello()

def hello(to=''):
    print("Hello," , to)

    main()