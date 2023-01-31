# Get user input
num = int(input("Enter a number: "))

# Initialize a counter variable
i = 0

# Start a while loop
while i <= num:
    # Check if the current number is odd or even
    if i % 2 == 0:
        # Print even
        print(i, "is even")
    else:
        # Print odd
        print(i, "is odd")

    # Increment the counter variable
    i += 1
