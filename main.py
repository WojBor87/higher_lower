import random
from art import logo, vs
from game_data import data
from replit import clear

def choose_data(*previous):
    '''
    Function that will choose one Name from data list and return it at the end. If something is already choose function will check if new item isn't equal to prevuious.
    '''
    current = random.choice(data)
    if previous:
        while current == previous:
            current = random.choice(data)
        return current
    else:
        return current

def check(a, b, anwser):
    '''
    function will check if player anwser correctly, if so it will return True if not will return False.
    '''
    if a['follower_count'] >= b['follower_count']:
        correct = "a"
    else:
        correct = "b"
    
    return anwser.lower() == correct
  

def print_info(account):
    '''
    Takes the account data and return the printable format
    '''
    return f"{account['name']}, a {account['description']} form {account['country']}"

again = True
while again:
    score = 0
    account1 = choose_data()
    next_turn = True

    while next_turn:
        clear()
        print(logo)
        if score > 0:
            print(f"You're right! Current score {score}")
        print(f"Compare A: " + print_info(account1))
        print(vs)
        account2 = choose_data(account1)
        print(f"Against B: " + print_info(account2))
        anwser = input("Who has more followers? Type 'A' or 'B': ")
        if check(account1, account2, anwser):
            score += 1
            print(score)
            item1 = account2
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score {score}")
            next_turn = False
    
    play_again = input("Do you want to play again? (Y or N)")
    if play_again not in ("Y", "y", "Yes", "yes"):
        again = False
