#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

NE_Farm= ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]

W_Farm= ["pigs", "chickens", "llamas"]

SE_Farm= ["chickens", "carrots", "celery"]

for filthyanimals in NE_Farm:
    print(filthyanimals)



for ranch in farms:
    print("-", "NE Farm",    "W Farm",    "SE Farm")
choice= input("Pick a farm!\n")

for ranch in farms:
    if farm["name"].lower() == choice.lower():
        print(NE_Farm)
