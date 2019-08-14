#game.py
#Plays the game 'Mastermind'
#
#Akshat Phumbhra
#10/3/2018
import random
NUM_TURNS=10

def Generate_Code(): #Returns a code
    # RED=0
    # GREEN=1
    # BLUE=2
    # YELLOW=3
    # PURPLE=4
    # ORANGE=5
    x1=random.randint(0,5)
    x2=random.randint(0,5)
    x3=random.randint(0,5)
    x4=random.randint(0,5)
    
    choice=input("Would you like to create your own code? Type Y for yes or N for no. \nIf you choose no, a random code will be generated for you to guess. " ).strip().upper()
    if choice=='Y':#Allows user to enter code
        code=input("Enter your code: ").strip().upper()
    elif choice=='N':#Generates a random code
        if x1==0:
            color1='R'
        elif x1==1:
            color1='G'
        elif x1==2:
            color1='B'
        elif x1==3:
            color1='Y'
        elif x1==4:
            color1='P'
        elif x1==5:
            color1='O'
        
        if x2==0:
            color2='R'
        elif x2==1:
            color2='G'
        elif x2==2:
            color2='B'
        elif x2==3:
            color2='Y'
        elif x2==4:
            color2='P'
        elif x2==5:
            color2='O'
            
        if x3==0:
            color3='R'
        elif x3==1:
            color3='G'
        elif x3==2:
            color3='B'
        elif x3==3:
            color3='Y'
        elif x3==4:
            color3='P'
        elif x3==5:
            color3='O'
            
        if x4==0:
            color4='R'
        elif x4==1:
            color4='G'
        elif x4==2:
            color4='B'
        elif x4==3:
            color4='Y'
        elif x4==4:
            color4='P'
        elif x4==5:
            color4='O'
        
        code=color1+color2+color3+color4
        
    return code

def print_Introduction():
    print("Welcome to my awesome Mastermind Game!")
    print("You have to guess a 4 color code out of 6 possible colors.")
    print("The colors are R, G, B, Y, P, O.")
    print()
    
def Clue(code,guess):
    black_counter=0
    white_counter=0
    while True:
        try:
            for i in range(4):
                if code[i]==guess[i]:
                    black_counter+=1
                    code=code[:i]+'x'+code[i+1:]
                    guess=guess[:i]+'y'+guess[i+1:]
            break
        except IndexError:
            print("Invalid input. Try again.")
            guess=input("Enter your guess: ").strip().upper()
    for i in range(4):
        for j in range(4):
            if code[i]==guess[j]:
                white_counter+=1
                code=code[:i]+'x'+code[i+1:]
                guess=guess[:j]+'y'+guess[j+1:]
    print("Not quite. You get", black_counter,"black pegs,", white_counter, "white pegs.")
    
def main():
    print_Introduction()
    
    code=Generate_Code()
    won= False
    num_guess=0
    
    while not won and num_guess<NUM_TURNS:
        guess=input("Enter your guess: ").strip().upper()
        if guess==code:
            won=True
            print("You win! So clever.")
        else:
            Clue(code,guess)
            if(num_guess==9):
                print("Sorry. You lose. You ran out of guesses.")
        num_guess+=1
    
    
    
main()