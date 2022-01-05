#!/usr/bin/env python3

#challenge writing code using if, elif, and else to determine personalty type

intro = 0
ext = 0

while True:
    response = input('Enter 1 for concert or 2 for netflix ')
    if response == "1":
        print("YOU ARE EXTROVERTED")
        ext += 1
        break
    elif response == "2":
        print("you are introverted")
        intro += 1
        break
    else:
        print("INVALID response")
        
print("Thanks for playing")
