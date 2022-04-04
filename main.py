from turtle import clear
from game_data import data
import random


def format_data(account):
    
    """ take the account data and returns the printable  formate.""" #docs string 
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return(f"{account_name}, is a {account_descr}, from {account_country}")

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns it they got it right."""
    if a_follower_count > b_follower_count:
        return guess=="a"
    else:
        return guess=="b"
    

score=0
game_should_continue=True
account_b=random.choice(data)
#make the game repeatable.

while game_should_continue:
        
    # Generate a random account from the game data.
    account_a=account_b  
    account_b=random.choice(data)   #here  we get a dictionary for the list

    while account_a == account_b:      #we need two separate dictionary thats why we use this formula
        account_b=random.choice(data)


    print(f"Compare A: {format_data(account_a)}.")
    print("VS")
    print(f"Against B: {format_data(account_b)}.")


    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    ## Get follower count.
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    is_correct= check_answer(guess,a_follower_count,b_follower_count)
    clear


    #give user feedback on thir guess.
    # Score Keeping.
    if is_correct:
        score+=1
        print(f"Your are right! Current Score: {score}")
    else:
        game_should_continue=False
        print(f"Doeey, that's wrong. Final score: {score}")

    