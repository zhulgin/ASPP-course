

class Mammals():
    def __init__(self):
        self.members = ["Cat", "Elephant", "Horse"]


    def printMembers(self):
        print("Printing members of the harmless mammals class")

        for member in self.members:
            print("\t%s " % member)