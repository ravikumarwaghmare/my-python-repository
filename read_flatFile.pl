##Description - Read flat file line by line in Python
##Developer - Ravikumar Waghmare 


import time

filename = "input_file.out"

file = open(filename, "r")

for line in file:
    print (line)
    time.sleep(10)
