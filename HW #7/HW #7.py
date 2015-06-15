import csv

def sameAB(string):
	if string == '':
		return True
	elif string[0] == 'a' and string[-1] == 'b':
		sameAB(string[1:-1])
	else:
		return False

def binary_search(lst, val):
	if val == lst[len(lst)/2]:
		return True
	elif val > lst[len(lst)/2] and val <= lst[len(lst)-1]:
		binary_search(lst[len(lst)/2:len(lst)], val)
	elif val < lst[len(lst)/2] and val >= lst[0]:
		binary_search(lst[0:len(lst)/2], val)
	else:
		return False

def flatten(lst):
	'''still have some problem'''
	if len(lst) == 1:
		return lst[0]
	else:
		lst[-2] = lst[-2] + lst[-1]
		lst.pop()
		flatten(lst)

def initials(lst):
	return [] if len(lst) == 0 else ['.'.join(word[0] for word in lst[0].split())]+initials(lst[1:])

def meamers(filename):
	return ([row[1] for row in csv.reader(open(filename, 'r'))]).count('MEAM')

def most_frequent_alphabet(frequency_dictionary):
	return ([key for key in frequency_dictionary])[([frequency_dictionary[key] for key in frequency_dictionary]).index(max([frequency_dictionary[key] for key in frequency_dictionary]))]

