class Fish():
    def __init__(self):
        self.members = ["Beastly bass", "Monsterous muikku", "Spooky salmon"]


    def printMembers(self):
        print("Printing members of the dangerous fish class")

        for member in self.members:
            print("\t%s " % member)