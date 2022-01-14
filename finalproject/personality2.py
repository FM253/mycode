#!/usr/bin/env python3

#challenge writing code using if, elif, and else to determine personalty type

#assingning variables
Introverted = 0
Extroverted = 0
Sensing = 0
Intuition = 0
Thinking = 0
Feeling = 0
Judging = 0
Perceiving = 0


while True:
    response = input('Enter 1 for concert or 2 for netflix ')
    if response == "1":
        Extroverted += 1
        break
    elif response == "2":
        Introverted += 1
        break
    else:
        print("INVALID response")
while True:
    response = input('Enter 1 for big party or 2 for small get together ')
    if response == "1":
        Extroverted += 1
        break
    elif response == "2":
        Introverted += 1
        break
    else:
        print("INVALID response")
while True:
    response = input('In coversation, enter 1 if you prefer to speak or 2 if you prefer to listen ')
    if response == "1":
        Extroverted += 1
        break
    elif response == "2":
        Introverted += 1
        break
    else:
        print("INVALID response")


while True:
    response = input('You are house shopping, enter 1 if you buy based on current condition or 2 if you buy based on future possibilities ')
    if response == "1":
        Sensing += 1
        break
    elif response == "2":
        Intuition += 1
        break
    else:
        print("INVALID response")
while True:
    response = input('Enter 1 if you prefer to take an accounting course or 2 if you prefer an acting lessons ')
    if response == "1":
        Sensing += 1
        break
    elif response == "2":
        Intuition += 1
        break
    else:
        print("INVALID response")
while True:
    response = input('When solving a problem, enter 1 if you review details to make a plan of action or 2 if you try different solutions and strategies ')
    if response == "1":
        Sensing += 1
        break
    elif response == "2":
        Intuition += 1
        break
    else:
        print("INVALID response")


while True:
    response = input('Enter 1 if you prefer fair judgement or 2 if you prefer compassion ')
    if response == "1":
        Thinking += 1
        break
    elif response == "2":
        Feeling += 1
        break
    else:
        print("INVALID response")
while True:
    response = input('When your friend has a relationship issue, enter 1 if you help your friend find a solution or 2 if you listen to understand ')
    if response == "1":
        Thinking += 1
        break
    elif response == "2":
        Feeling += 1
        break
    else:
        print("INVALID response")
while True:
    response = input('To persuade you, enter 1 if an emotional appeal works better or 2 if a logical explanation works better ')
    if response == "1":
        Thinking += 1
        break
    elif response == "2":
        Feeling += 1
        break
    else:
        print("INVALID response")


while True:
    response = input('Enter 1 if you plan your travel in great detail or 2 if you go with the flow when travelling ')
    if response == "1":
        Judging += 1
        break
    elif response == "2":
        Perceiving += 1
        break
    else:
        print("INVALID response")
while True:
    response = input('Enter 1 if your car is clean more often or 2 if it is untidy more often ')
    if response == "1":
        Judging += 1
        break
    elif response == "2":
        Perceiving += 1
        break
    else:
        print("INVALID response")
while True:   
    response = input('Enter 1 if you make decisions quickly or 2 if you take your time to consider different factors ')
    if response == "1":
        Judging += 1
        break
    elif response == "2":
        Perceiving += 1
        break
    else:
        print("INVALID response")


if Extroverted > Introverted:
    print("E")
if Introverted > Extroverted:
    print("I")


if Sensing > Intuition:
    print("S")
if Intuition > Sensing:
    print("N")


if Thinking > Feeling:
    print("T")
if Feeling > Thinking:
    print("F")


if Judging > Perceiving:
    print("J")
if Perceiving > Judging:
    print("P")

print("These are your personality type characters")
print("For more info visit https://www.mbtitest.com/#16-personality-types-characters")
