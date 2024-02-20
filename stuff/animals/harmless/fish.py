class Fish():
    def __init__(self):
        self.members = ["Bass", "Muikku", "Salmon"]


    def printMembers(self):
        print("Printing members of the harmless fish class")

        for member in self.members:
            print("\t%s " % member)