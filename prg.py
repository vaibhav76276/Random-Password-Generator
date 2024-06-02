import string  # Importing string module to handle string constants
import random  # Importing random module to generate random numbers

# Define character sets
alpha = "abcdefghijklmnopqrstuvwxyz"  # Lowercase alphabet characters
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Uppercase alphabet characters
character = "!@#$%^&*()_+-=\/?"       # Special characters
numbers = "1234567890"                # Numeric characters

# Initialize variables
i = 0  # Counter for the while loop
p = 0  # Unused in the current implementation but initialized for consistency
characters = alpha + ALPHA + character + numbers  # Combine all characters into one string

# Prompt the user to enter the desired length of the password
length = int(input("Enter the length of password:"))

# Initialize an empty password string
password = ""

# Ensure the password starts with a random lowercase letter
x = random.randint(0, 25)  # Generate a random index for lowercase letters
password += alpha[x]       # Append the selected lowercase letter to the password

# Generate the remaining characters of the password
while i != length - 2:
    b = random.choice(characters)  # Randomly select a character from the combined set
    password += b                  # Append the selected character to the password
    i += 1                         # Increment the counter

# Ensure the password ends with a random uppercase letter
A = random.randint(0, 25)  # Generate a random index for uppercase letters
password += ALPHA[A]       # Append the selected uppercase letter to the password

# Print the generated password
print(password)

