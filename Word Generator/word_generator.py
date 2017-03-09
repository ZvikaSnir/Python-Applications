import string
import random

vowels = "oeiouy"
consonants = "bcdfghjklmnpqrstvwxz"
letters = string.ascii_lowercase

input_one = input("Enter 1 for vowel, 2 for consenant, or 3 for any.")
input_two = input("Enter 1 for vowel, 2 for consenant, or 3 for any.")
input_three = input("Enter 1 for vowel, 2 for consenant, or 3 for any.")


def generator():
	if input_one == '1':
		res = random.choice(vowels)
	elif input_one == '2':
		res = random.choice(consonants)
	else:
		res = random.choice(letters)

	if input_two == '1':
		res += random.choice(vowels)
	elif input_two == '2':
		res += random.choice(consonants)
	else:
		res += random.choice(letters)

	if input_three == '1':
		res += random.choice(vowels)
	elif input_three == '2':
		res += random.choice(consonants)
	else:
		res += random.choice(letters)

	return res


for times in range(10):
	print(generator())