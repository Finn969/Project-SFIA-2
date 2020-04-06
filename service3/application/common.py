"""Bullshit Generator, by Michael Sproul."""

import random

vowels = {"a", "e", "i", "o", "u"}

def choose_uniq(exclude, *args):
	"""Choose a unique random item from a variable number of lists."""
	item = choose_from(*args)
	while item in exclude:
		item = choose_from(*args)
	return item


def choose_from(*args):
	"""Choose a random item from any number of lists."""
	biglist = []
	for l in args:
		biglist = biglist + l
	i = random.randint(0, len(biglist) - 1)
	return biglist[i]


def sentence_case(sentence, exciting=False):
	"""Capitalise the first letter of the sentence and add a full stop."""
	sentence = sentence[0].upper() + sentence[1:]

	if sentence[-1] in {'.', '!', '?'}:
		return sentence
	elif exciting:
		return sentence + "!"
	else:
		return sentence + "."


def ing_to_ed(word):
	"""Convert `ing' endings to `ed' endings."""
	if word[-3:] == "ing":
		return (word[:-3] + "ed")
	else:
		return word


def an(word):
	"""Prefix with 'a' or 'an', as appropriate."""
	if word[0] in vowels:
		return "an %s" % word
	else:
		return "a %s" % word
