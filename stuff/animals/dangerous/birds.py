



class Birds():
    def __init__(self):
        self.members = ["Spooky sparrow", "Reckless robin", "Devious duck"]


    def printMembers(self):
        print("Printing members of the dangerous birds class")

        for member in self.members:
            print("\t%s " % member)