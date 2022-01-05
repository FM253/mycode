#!/usr/bin/env python3

#challenge writing code using if, elif, and else to determine personalty type



intro = 0
ext = 0




while True:
    response = input('Enter 1 for concert or 2 for netflix ')
    if response == "1":
        ext += 1
        break
    elif response == "2":
        intro += 1
        break
    else:
        print("INVALID response")




while True:
    response = input('Enter 1 for big party or 2 for small get together ')
    if response == "1":
        ext += 1
        break
    elif response == "2":
        intro += 1
        break
    else:
        print("INVALID response")




while True:
    response = input('In coversation, enter 1 if you prefer to speak or 2 if you prefer to listen ')
    if response == "1":
        ext += 1
        break
    elif response == "2":
        intro += 1
        break
    else:
        print("INVALID response")


if ext > intro:
    print("you are EXTROVERTED!")
if intro > ext:
    print("YOU ARE introverted")


print("Thanks for playing")
