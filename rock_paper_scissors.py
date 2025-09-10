# Rock Paper Scissors Game
#################################################################################################
print("""
    _______                         _______                            _______
---'   ____)                   ---'    ____)____                   ---'   ____)____
      (_____)                             ______)                             ______)
      (_____)                            _______)                          __________)
      (____)                            _______)                         (____)
---.__(___)                    ---.__________)                     ---.__(___)
""")

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
#################################################################################################
import random

while True:  # main game loop for replay
    lives = int(input("How many lives do you want to play with? \n"))
    player_lives = lives
    cpu_lives = lives

    while player_lives > 0 and cpu_lives > 0:
        player_move = input("What do you choose: Rock, Paper, or Scissors? \n").lower()
        if player_move not in ["rock", "paper", "scissors"]:
            print("Invalid choice, try again.")
            continue

        cpu_move = random.choice(["rock", "paper", "scissors"])
        print(f"You: {player_move} | Computer: {cpu_move}")

        # Show player's choice as ASCII
        if player_move == "rock":
            print(rock)
        elif player_move == "paper":
            print(paper)
        else:
            print(scissors)

        # Show computer's choice as ASCII
        if cpu_move == "rock":
            print(rock)
        elif cpu_move == "paper":
            print(paper)
        else:
            print(scissors)

        # Logic
        if cpu_move == player_move:
            print("It's a tie")
        elif player_move == "rock" and cpu_move == "scissors":
            print("You win this round!")
            cpu_lives -= 1
        elif player_move == "scissors" and cpu_move == "paper":
            print("You win this round!")
            cpu_lives -= 1
        elif player_move == "paper" and cpu_move == "rock":
            print("You win this round!")
            cpu_lives -= 1
        else:
            print("Computer wins this round!")
            player_lives -= 1

        print(f"You have {player_lives} lives left.")
        print(f"Computer has {cpu_lives} lives left.")
        print("*" * 40)

    # End of one game
    if player_lives == 0:
        print("You lost the game 😢")
    else:
        print("You won the game 🎉")

    # Ask if player wants to play again
    again = input("Do you want to play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing! 👋")
        break
