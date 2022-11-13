class Father:
    def skills(self):
        print('gardening, programming')


class Mother:
    def skills(self):
        print('cooking art')


class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")


c = Child()
c.skills()
