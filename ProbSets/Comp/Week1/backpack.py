class Backpack:

    def __init__(self, name, color, max_size = 5):
        self.name = name
        self.contents = []
        self.color = color
        self.max_size = max_size

    def put(self, item):
        if(len(self.contents) <= self.max_size):
            self.contents.append(item)
        elif(len(self.contents)> self.max_size):
            print("No Room!")

    def remove(self, item):
        self.contents.remove(item)

    def dump(self):
        self.contents = []

mybackpack = Backpack("Tom","Green")


mybackpack.put("pencil")

mybackpack.put("notebook")

mybackpack.put("lunch")

mybackpack.put("coat")

mybackpack.put("pens")

mybackpack.contents
