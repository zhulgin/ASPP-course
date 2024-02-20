

class Mammals():
    def __init__(self):
        self.members = ["Lion", "Tiger", "Wolf"]


    def printMembers(self):
        print("Printing members of the dangerous mammals class")

        for member in self.members:
            print("\t%s " % member)