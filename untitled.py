class Student(object):
	"""docstring for Student"""
	def __init__(self, name, age, SSN = 0):
		super(Student, self).__init__()
		self.name = name
		self.age = age
		self.SSN = SSN

f = open('asdf.txt','r')
studList = []
for line in f:
	studList.append(Student(line.split()[0],line.split()[1]))
print studList