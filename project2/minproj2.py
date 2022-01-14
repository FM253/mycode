#!/usr/bin/env python3


#opening .txt file in read mode
file = open("brett_comics.txt", "r")


#reading first 63 characters in file and printing to CLI
print(file.read(63))


#closing file
file.close()
