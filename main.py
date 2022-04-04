from game_data import data
import random

def format_data(account):
    
    """Format account data into printable format""" #docs string 
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return (f"{account_name}, is a {account_descr}, from {account_country}")



# Generate a random account from the game data.
account_a=random.choice(data)   #here  we get a dictionary for the list
account_b=random.choice(data)   #here  we get a dictionary for the list
if account_a == account_b:      #we need two separate dictionary thats why we use this formula
    account_b=random.choice(data)


print(f" Compare A: {format_data(account_a)}.")
print(f" Compare B: {format_data(account_b)}.")


# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.


# Score Keeping.

# Make game repeatable.


# Make B become the next A.

# Clear screen between rounds.