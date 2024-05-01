class CardPile:
    def __init__(self):
        self.items = []

    def add_top(self, item):
        self.items.insert(0, item)

    def add_bottom(self, item):
        self.items.insert(self.size(), item)

    def remove_top(self):
        return self.items.pop(0)

    def remove_bottom(self):
        return self.items.pop(self.size()-1)

    def size(self):
        return len(self.items)

    def peek_top(self):
        return str(self.items[0])

    def peek_bottom(self):
        return str(self.items[self.size()-1])

    def print_all(self, index):
        if index == 0:
            print (str(self.items[0]) + ' *'*(self.size()-1))
        else:
            temp = [str(x) for x in self.items]
            print (' '.join(temp))
