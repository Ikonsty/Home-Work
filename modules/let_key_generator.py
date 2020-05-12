from random import randint
from pprint import pprint

alphabet = {}

# dict_size = 128
# dict = {chr(i): i for i in range(dict_size)}
# pprint(dict)

for i in range(33, 64):
    rand_cord = '(' + str(randint(1, 10)) + ',' + str(randint(1, 10)) + ')'
    while rand_cord in alphabet.values():
        rand_cord = '(' + str(randint(1, 10)) + ',' + str(randint(1, 10)) + ')'
    alphabet[chr(i)] = rand_cord
for i in range(65, 91):
    rand_cord = '(' + str(randint(1, 10)) + ',' + str(randint(1, 10)) + ')'
    while rand_cord in alphabet.values():
        rand_cord = '(' + str(randint(1, 10)) + ',' + str(randint(1, 10)) + ')'
    alphabet[chr(i)] = rand_cord
for i in range(97, 123):
    rand_cord = '(' + str(randint(1, 10)) + ',' + str(randint(1, 10)) + ')'
    while rand_cord in alphabet.values():
        rand_cord = '(' + str(randint(1, 10)) + ',' + str(randint(1, 10)) + ')'
    alphabet[chr(i)] = rand_cord

f = open("letter_key_part2.txt", "w+")
for let in alphabet:
    f.write("{} {}\n".format(let, alphabet[let]))
f.close()
