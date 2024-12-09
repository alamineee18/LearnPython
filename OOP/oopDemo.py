class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Create a Person instance
x = Person("John", "Doe")
x.printname()

class Student(Person):
    def __init__(self, fname, lname, id, result, city):
        # Call the parent class constructor
        super().__init__(fname, lname)
        self.id = id
        self.result = result
        self.city = city

    def identity(self):
        print("ID:", self.id, "Result:", self.result, "City:", self.city)

# Create a Student instance
y = Student("Alamin", "Kabir", "18142", "3.32", "Rajshahi")
y.printname()
y.identity()
