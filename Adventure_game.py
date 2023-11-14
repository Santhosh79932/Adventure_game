#Text-Based Adventure Game

#import the time for creating delays 
import time

#define the function to explaim about the game 
def introduction():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1)
    print("You wake up in a mysterious land with a foggy memory.")
    time.sleep(1)
    print("Your goal is to explore, make choices, and discover the secrets of this land.")
    time.sleep(1)
    print("Type the number corresponding to your choice and press Enter to make a decision.")
    time.sleep(1)
    
#define the function for make_choices to user 
def make_choice(choices):
    print("\nChoose your action:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

#implement error handling for invalid inputs
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def explore_land():
    print("\nYou begin to explore the mysterious land.")
    time.sleep(1)
    choices = ["Enter the dark forest", "Follow the winding river"]
    choice = make_choice(choices)

    if choice == 1:
        print("You enter the dark forest.")
        time.sleep(1)
        dark_forest()
    else:
        print("You follow the winding river.")
        time.sleep(1)
        river_bank()

def dark_forest():
    print("\nYou find yourself in a dense and dark forest.")
    time.sleep(1)
    choices = ["Search for a path", "Try to climb a tree for a better view"]
    choice = make_choice(choices)

    if choice == 1:
        print("You search for a path through the forest.")
        time.sleep(1)
        bear_encounter()
    else:
        print("You attempt to climb a tree for a better view.")
        time.sleep(1)
        bird_nest()

def river_bank():
    print("\nYou arrive at the tranquil river bank.")
    time.sleep(1)
    choices = ["Build a raft and cross the river", "Follow the river downstream"]
    choice = make_choice(choices)

    if choice == 1:
        print("You decide to build a raft and cross the river.")
        time.sleep(1)
        treasure_island()
    else:
        print("You follow the river downstream.")
        time.sleep(1)
        waterfall()

def bear_encounter():
    print("\nAs you navigate through the forest, you encounter a bear!")
    time.sleep(1)
    choices = ["Attempt to run", "Stay still and remain calm"]
    choice = make_choice(choices)

    if choice == 1:
        print("You attempt to run from the bear.")
        time.sleep(1)
        print("The bear catches up, and you're injured. Game over!")
    else:
        print("You stay still and remain calm.")
        time.sleep(1)
        print("The bear loses interest and leaves. You continue your journey.")
        time.sleep(1)
        explore_land()

def bird_nest():
    print("\nWhile climbing the tree, you discover a bird's nest.")
    time.sleep(1)
    choices = ["Take some eggs", "Leave the nest undisturbed"]
    choice = make_choice(choices)

    if choice == 1:
        print("You decide to take some eggs from the nest.")
        time.sleep(1)
        print("The mother bird attacks you. Game over!")
    else:
        print("You leave the nest undisturbed.")
        time.sleep(1)
        explore_land()

def treasure_island():
    print("\nYou successfully cross the river and arrive at a hidden island.")
    time.sleep(1)
    print("You discover a treasure chest!")
    time.sleep(1)
    print("Congratulations! You have completed the adventure.")

def waterfall():
    print("\nAs you follow the river downstream, you encounter a magnificent waterfall.")
    time.sleep(1)
    choices = ["Climb the waterfall", "Find a way around the waterfall"]
    choice = make_choice(choices)

    if choice == 1:
        print("You attempt to climb the waterfall.")
        time.sleep(1)
        print("Unfortunately, you slip and fall. Game over!")
    else:
        print("You find a way around the waterfall.")
        time.sleep(1)
        explore_land()

# Main game loop
def play_game():
    introduction()
    explore_land()

# Run the game
if __name__ == "__main__":
    play_game()
