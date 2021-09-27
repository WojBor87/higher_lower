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
    
    if anwser.lower() == correct:
        return True
    else:
        return False

def print_info(item):
    '''
    Function prints information about item.
    '''
    return f"{item['name']}, a {item['description']} form {item['country']}"

again = True
while again:
    score = 0
    item1 = choose_data()
    next_turn = True

    while next_turn:
        clear()
        print(logo)
        if score > 0:
            print(f"You're right! Current score {score}")
        print(f"Compare A: " + print_info(item1))
        print(vs)
        item2 = choose_data(item1)
        print(f"Against B: " + print_info(item2))
        anwser = input("Who has more followers? Type 'A' or 'B': ")
        if check(item1, item2, anwser):
            score += 1
            print(score)
            item1 = item2
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score {score}")
            next_turn = False
    
    play_again = input("Do you want to play again? (Y or N)")
    if play_again not in ("Y", "y", "Yes", "yes"):
        again = False