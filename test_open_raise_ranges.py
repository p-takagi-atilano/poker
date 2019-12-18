import json
import random

POSITION_ORDER = ["UTG", "UTG+1", "UTG+2", "LJ", "HJ", "CO", "BTN", "SB"]

CARD_TYPES = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
CARD_SUITS = ["s", "o"]

with open("open_raise_ranges.json", 'r') as f:
		OPEN_RAISE_RANGES = json.loads(f.read())

def generate_random_hand():
	a = random.choice(CARD_TYPES)
	b = random.choice(CARD_TYPES)
	if a == b:
		return "{}{}".format(a, a)

	a,b = sorted([CARD_TYPES.index(a), CARD_TYPES.index(b)])
	a = CARD_TYPES[a]
	b = CARD_TYPES[b]
	return "{}{}s".format(b, a)

	'''
	a = random.choice(CARD_TYPES)
	b = random.choice(CARD_TYPES)
	if a == b:
		return "{}{}".format(a,b)
	
	ai = CARD_TYPES.index(a)
	bi = CARD_TYPES.index(b)
	if ai > bi:
		return "{}{}{}".format(a, b, random.choice(CARD_SUITS))
	return "{}{}{}".format(b, a, random.choice(CARD_SUITS))
	'''

def full_test():
	correct = 0
	total = 0

	while(True):
		result = single_test()
		if result:
			correct += 1
		total += 1

		print(result)
		print("{}/{}".format(correct, total))

def single_test():
	position = random.choice(POSITION_ORDER)
	hand = generate_random_hand()
	
	print("----------------")
	print("{}: {}".format(position, hand))
	
	response = input("> ")
	in_range = is_in_range(position, hand)

	return (response == "r" and in_range) or (response == "f" and not in_range)

	
def is_in_range(position, hand):
	for i in range(POSITION_ORDER.index(position) + 1):
		if hand in OPEN_RAISE_RANGES[POSITION_ORDER[i]]:
			return True
	return False

full_test()