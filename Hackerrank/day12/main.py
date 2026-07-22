class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNum, scores):
        super().__init__(firstName,lastName,idNum)
        
        self.scores = scores
    
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        sum(self.scores)
        len(self.scores)
        promedio = sum(self.scores) / len(self.scores)
        if  90 <=  promedio <= 100:
            return 'O'
        elif 80 <= promedio < 90:
            return 'E'
        elif 70 <= promedio < 80:
            return 'A'
        elif 55 <= promedio < 70:
            return 'P'
        elif 40 <= promedio < 55:
            return 'D'
        else:
            return 'T'
    
        
line = input("Dame tu nombre y tu apellido").split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input("Dame tus notas para calcularte tu promedio y verificarte si aprobaste")) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())