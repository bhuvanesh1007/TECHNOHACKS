import random
user_choice = input("enter your choice (rock,paper,scissors): ")
user_choice = user_choice.lower()
avail_choices = ["rock","paper","scissors"]
comp_choice = random.choice(avail_choices)
print(f"computer chose : {comp_choice}")

if user_choice == comp_choice:
    print(f"Both players selected {user_choice}. It's a tie.")
elif user_choice == "rock":
    if comp_choice == "scissors" :
        print("Rock smashes scissors. user won.")
    else:
        print("paper covers rock.computer won")
elif user_choice == "paper":
    if comp_choice == "rock":
        print("paper covers rock. user won.")
    else:
        print("scissors cuts paper. computer won.")
elif user_choice == "scissors":
    if comp_choice == "rock":
        print("rock smashes scissors. computer won.")
    else:
        print("scissor cuts paper. user won.")