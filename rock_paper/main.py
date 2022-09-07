#imporring random library
import random      


#define functioin to get choices
def get_choices():
    player_choice= input("enter a choice(rock,paper,choice):")

    #genarating random choices 
    computer_choice=random.choice(["paper","rock","scissor"])

    #choices is a dictionary having (key= player and computer) and data
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player,computer):
    #f = fstring to place string and variable in the bracket
    print(f"you choose {player}, computer chooses {computer}")
    
    if player==computer:
        return "it's tie"
    
    elif player=="rock":
        
        if computer=="scissor":
            return "player win"
        else:
            return "computer win"
    
    elif player=="paper":
        
        if computer=="rock":
            return "player win"
        else:
            return "computer win"
    else:
        if computer=="rock":
            return "computer wins"
        else:
            return "computer wins"

#calling the get_choices function
choice=get_choices()

#accessing check_win function and passing the argument from dictionary key
result = check_win(choice["player"], choice["computer"])
print(result)

    
    