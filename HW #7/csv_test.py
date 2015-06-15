import csv

def meamers(filename):
	return ([]+[row[1] for row in csv.reader(open(filename, 'r'))]).count('MEAM')

def main():
	print meamers('studentfile.csv')

if __name__ == '__main__':
	main()