import random
from string import digits, ascii_uppercase as letters


"""
Difficult to remember number plates (kolgomoro complexity)

Requirements
	minimum: [A-Z0-9 ]{2, 7}    (use max count)
	
	first char is letter
	no dupes (except spaces, see below)
	no vowels (except ÆØÅ, see below)
	no sequence (abc, 456)
	random if space (max 1, must be at 2, 3, 4)
	one 'ÆØÅ' at 0, 1, 5, or 6
	for each pos beyond index 0: 
		letter chance: current plate num count / current plate letter count
			if not at a space-position, then there is a 50% chance for a space
				unless it's the last available space-pos, then that is a guaranteed space

		nums:
			no even nums at even pos index (starting at 0)
"""


# strip vowels
letters = "".join([c for c in letters if c not in "AEIOUY"])


def gen_plate():
	plate = ""
	for i in range(7):
		# first char, a letter
		if i == 0:
			plate += random.choice(letters)
			continue
			
		# space chance
		if i in (2, 3, 4):
			if not " " in plate:
				if random.random() < 1/4:
					# place space
					plate += " "
					continue
		
		current_letters = len([c for c in plate if c in letters])
		current_numbers = len([c for c in plate if c in digits])
		letter_chance = current_numbers / current_letters
		
		if random.random() < letter_chance:
			# place a letter
			avail = [c for c in letters if c not in plate]  # shallow copy + remove dupes
			# avoid a sequence
			seq_next = letters[(letters.index(plate[-1]) + 1) % len(letters)] if plate[-1] in letters else None
			if seq_next is not None and seq_next in avail:
				avail.remove(seq_next)
			
			char = random.choice(avail)
		else:
			# place a number
			avail = [d for d in digits if d not in plate]  # shallow copy + remove dupes
			# avoid a sequence
			seq_next = digits[(digits.index(plate[-1]) + 1) % len(digits)] if plate[-1] in digits else None
			if seq_next is not None and seq_next in avail:
				avail.remove(seq_next)
			
			char = random.choice(avail)
			
		plate += char
	
	# place one special character
	index = random.choice((0, 1, 5, 6))
	plate = plate[:index] + random.choice("ÆØÅ") + plate[index+1:]
	
	return plate


if __name__ == "__main__":
	for i in range(25):
		print("\t" + gen_plate())

