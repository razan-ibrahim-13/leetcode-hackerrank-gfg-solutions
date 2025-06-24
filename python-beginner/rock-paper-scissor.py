import random

s = "y"
while s=="y":
    choices = ["r", "p", "s"]
    computer_choice = random.choice(choices)

    your_choice = input("rock,paper,scissor ? (r/p/s)")

    if your_choice == "r" and computer_choice == "r":
        print("your choice = rock \ncomputer choice = rock ")
        print("no point")
        s = input("you want to continue ? (y/n) : ")
    elif your_choice == "p" and computer_choice == "p":
        print("your choice = paper \ncomputer choice = paper ")
        print("no point")
        s = input("you want to continue ? (y/n) : ")
    elif your_choice == "s" and computer_choice == "s":
        print("your choice = scissor \ncomputer choice = scissor ")
        print("no point")
        s = input("you want to continue ? (y/n) : ")
    elif your_choice == "p" and computer_choice == "r":
        print("your choice = paper \ncomputer choice = rock ")
        print("you got the point")
        s = input("you want to continue ? (y/n) : ")
    elif your_choice == "p" and computer_choice == "s":
        print("your choice = paper \ncomputer choice = scissor ")
        print("computer got the point")
        s = input("you want to continue ? (y/n) : ")
    elif your_choice == "r" and computer_choice == "p":
        print("your choice = rock \ncomputer choice = paper")
        print("computer got the point")
        s = input("you want to continue ? (y/n) : ")
    elif your_choice == "r" and computer_choice == "s":
        print("your choice = rock \ncomputer choice = scissor ")
        print("you got the point")
        s = input("you want to continue ? (y/n) : ")
    elif your_choice == "s" and computer_choice == "p":
        print("your choice = scissor \ncomputer choice = paper ")
        print("you got the point")
        s = input("you want to continue ? (y/n) : ")
    elif your_choice == "s" and computer_choice == "r":
        print("your choice = scissor \ncomputer choice = rock ")
        print("computer got the point")
        s = input("you want to continue ? (y/n) : ")
    else :
        print("enter a valid choice")
        s = input("you want to continue ? (y/n) : ")







