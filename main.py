import random
import json

def data_load():
    with open("master.json", "r") as f:
        return json.load(f)
    
def game(data):
    correct_answers = 0
    incorrect_answers = 0

    random.shuffle(data)

    for item in data:
        answer = input(f"What anime is {item['CharName']} in?")

        if answer == str(item['AnimeName']):
            correct_answers += 1
            print("Correct!")
        else:
            incorrect_answers += 1
            print("Incorrect!")
        
    print(f"Game over! You got {correct_answers} correct and {incorrect_answers} incorrect.")

    data = data_load()

    while True:
        print("Hello! Welcome to the anime quiz! Can you guess the anime from the character name?")

        game(data)

        replay_game = input("Would you like to play again? (y/n)").upper()
        if replay_game.upper() != "Y":
            break
