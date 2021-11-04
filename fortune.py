
import random

"""
Fortune - a fortune telling program.
this is a simple python fortune teller.

it reads a file named "fortunedat.txt" it picks a random fortune from that file. it prints out the fortune for the user.

to run it, type in a shell, python3 fortune.py
"""

file_content = open('fortunedat.txt','r')
content_str = file_content.read()
quotes_list = content_str.split("%\n")
str_ind= len(quotes_list)-1

#print(str_ind)

position = random.randrange(str_ind)

#print(position)

#print(type(quotes_list))

print(quotes_list[position])