class Person:

    # Constructor
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Driver code
v = Person("CSE", "PFSD")
v.printname()