
class Human:
    def __init__(self, n, o):
        self.name = n;
        self.occupoation = o

    def do_work(self):
        if self.occupoation == "tennis player":
            print(self.name, "play tennis")
        elif self.occupoation == "actor":
            print(self.name, "shoot film")

    def speaks(self):
        print(self.name, "say how are you?")


tom = Human("tom cruise", "actor")
tom.do_work()
tom.speaks()

maria = Human("Mario Sharapova", "tennis player")
maria.do_work()
maria.speaks()

s = "I work in bloomberg founded by bloomberg work"

tokens = s.split(" ")
d = {}
for token in tokens:
    if token in d:
        d[token] += 1
    else:
        d[token] = 1
print(d)

