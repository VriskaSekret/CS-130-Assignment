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
            if self.size() > 0:
                temp = [str(x) for x in self.items]
                print (' '.join(temp))


class Solitaire:
    def __init__(self, cards):
        self.piles = []
        self.num_cards = len(cards)
        self.num_piles = (self.num_cards // 8) + 3
        self.max_num_moves = self.num_cards * 2
        for i in range(self.num_piles):
            self.piles.append(CardPile())
        for i in range(self.num_cards):
            self.piles[0].add_bottom(cards[i])

    def get_pile(self, i):
        return self.piles[i]

    def display(self):
        for i in range(self.num_piles):
            if self.get_pile(i).size() > 0:
                print (f'{i}: ', end = '')
                self.get_pile(i).print_all(i)
            else:
                print (f'{i}: ')

    def move(self,p1,p2):
        pile_1 = self.get_pile(p1)
        pile_2 = self.get_pile(p2)
        if (p1 == p2 and p2 == 0):
            if pile_1.size() != 0:
                moved_card = pile_1.remove_top()
                pile_2.add_bottom(moved_card)
        elif (p1 == 0 and p2 > 0):
            if (pile_1.size() != 0):
                if (pile_2.size() != 0 and
                    pile_1.items[0] == pile_2.items[pile_2.size()-1]-1):
                    moved_card = pile_1.remove_top()
                    pile_2.add_bottom(moved_card)
                elif (pile_2.size() == 0):
                    moved_card = pile_1.remove_top()
                    pile_2.add_bottom(moved_card)
        elif (p1 > 0 and p2 > 0):
            if (pile_1.size() > 0 and
                pile_2.size() > 0 and
                pile_1.items[0] == pile_2.items[pile_2.size()-1]-1):
                for i in range(pile_1.size()):
                    moved_card = pile_1.remove_top()
                    pile_2.add_bottom(moved_card)
    
    def is_complete(self):
        pile_0 = self.get_pile(0)
        if (pile_0.size() == 0):
            for i in range(self.num_piles):
                if self.get_pile(i).size() == self.num_cards:
                    return True
        return False

    def play(self):
        print("********************** NEW GAME *****************************")
        move_number = 1
        while move_number <= self.max_num_moves and not self.is_complete():
            self.display()
            print("Round", move_number, "out of", self.max_num_moves, end = ": ")
            pile1 = int(input("Move from pile no.: "))
            print("Round", move_number, "out of", self.max_num_moves, end = ": ")
            pile2 = int(input("Move to pile no.: "))
            if pile1 >= 0 and pile2 >= 0 and pile1 < self.num_piles and pile2 < self.num_piles:
                self.move(pile1, pile2)
            move_number += 1
            #implementing saving
            self.save(move_number)
            
        if self.is_complete():
            print("You Win in", move_number - 1, "steps!\n")
            self.clear_save()
        else:
            print("You Lose!\n")
            self.clear_save()
#
#required variables to be saved
#card pile amount
#values in each pile
#current move
#

    #saves into the save.txt file, each line is a different variable
    def save(self, move_number):
        f = open('save.txt', 'w')
        f.write(str(move_number) + '\n')
        f.write(str(self.num_piles) + '\n')
        for i in range(len(self.piles)):
            if len(self.piles[i].items) > 0:
                for k in self.piles[i].items:
                    f.write(str(k) + ' ')
                f.write('\n')
            else:
                f.write('EMPTY\n')
        f.close()
    #loads game from the save.txt file
    def load(self):
        print("********************** LOADED GAME *****************************")
        f = open('save.txt', 'r')
        line_list = list(f)
        f.close()

    def clear_save(self):
        open('save.txt', 'w').close()


cards = [5, 13, 9, 6, 12, 8, 11, 14, 10, 7, 1, 2, 0, 3, 4]
game = Solitaire(cards)
game.play()



##f = open('save.txt', 'r')
##line_list = list(f)
##f.close()
##print (line_list)
##






