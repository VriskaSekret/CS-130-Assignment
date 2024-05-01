##
##  Geoff Ribu
##  UPI - grib784
##  ID - 926605515
##  Solitaire Section 5
##
import random

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
        save_file = open('save.txt', 'r')
        line_list = list(save_file)
        save_file.close()
        #if save file is empty it starts a new instance of the game
        if (line_list[0] == 'NO DATA'):
            self.move_number = 1
            #variable to check whether the game is new or from a saved file
            self.loaded = False
            self.piles = []
            self.num_cards = len(cards)
            self.num_piles = (self.num_cards // 8) + 3
            self.max_num_moves = self.num_cards * 2
            for pile_index in range(self.num_piles):
                self.piles.append(CardPile())
            for card in range(self.num_cards):
                self.piles[0].add_bottom(cards[card])
        #if there is a save in save.txt it allows it to be loaded
        else:
            self.move_number = 1
            #variable to check whether the game is new or from a saved file
            self.loaded = True
            self.piles = []
            self.num_cards = 0
            self.max_piles = 0
            self.max_num_moves = 0

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
            for pile_index in range(self.num_piles):
                if self.get_pile(pile_index).size() == self.num_cards:
                    return True
        return False

    def play(self):
        #checks if the game is to be loaded or new
        if self.loaded == False:
            print("********************** NEW GAME *****************************")
            self.move_number = 1
        else:
            self.load()
        while self.move_number <= self.max_num_moves and not self.is_complete():
            self.display()
            print("Round", self.move_number, "out of", self.max_num_moves, end = ": ")
            pile1 = int(input("Move from pile no.: "))
            print("Round", self.move_number, "out of", self.max_num_moves, end = ": ")
            pile2 = int(input("Move to pile no.: "))
            if pile1 >= 0 and pile2 >= 0 and pile1 < self.num_piles and pile2 < self.num_piles:
                self.move(pile1, pile2)
            self.move_number += 1
            #saves the game state after each move
            self.save()
            
        if self.is_complete():
            print("You Win in", self.move_number - 1, "steps!\n")
        else:
            print("You Lose!\n")

        
#
#variables are saved in the following format
#
#current move
#card pile amount
#amount of cards total
#values in each respective pile
#

    #saves game state into the save.txt file, each line is a different variable
    def save(self):
        save_file = open('save.txt', 'w')
        save_file.write(str(self.move_number) + '\n')
        save_file.write(str(self.num_piles) + '\n')
        save_file.write(str(self.num_cards) + '\n')
        for pile_index in range(len(self.piles)):
            if len(self.piles[pile_index].items) > 0:
                for card in self.piles[pile_index].items:
                    save_file.write(str(card) + ' ')
                save_file.write('\n')
            else:
                save_file.write('EMPTY\n')
        save_file.close()
        
    #loads game from the save.txt file
    def load(self):
        print("********************** LOADED GAME *****************************")
        save_file = open('save.txt', 'r')
        line_list = list(save_file)
        save_file.close()
        #removes whitespace from data 
        for line_index in range(len(line_list)):
            line_list[line_index] = line_list[line_index].strip()
        #assigning each variable
        self.move_number = int(line_list.pop(0))
        self.num_piles = int(line_list.pop(0))
        self.num_cards = int(line_list.pop(0))
        self.max_num_moves = self.num_cards * 2
        #creating a list of cardpiles for the game
        [self.piles.append(CardPile()) for x in range(self.num_piles)]
        #filling each card pile with their respective piles from save data
        for pile_string_index in range(len(line_list)):
            if line_list[pile_string_index] != 'EMPTY':
                line_list[pile_string_index] = line_list[pile_string_index].split()
        for i in range(self.num_piles):
            for card in line_list[i]:
                if card.isdigit():
                    self.piles[i].add_bottom(int(card))

        
#clears the save file
def clear_save():
        f = open('save.txt', 'w')
        f.write('NO DATA')
        f.close()
    
#asks user if they want to continue playing
def prompt_user():
    continue_playing = ''
    while True:
        continue_playing = input('Continue Playing? (Y/N): ')
        if continue_playing == 'Y':
            return True
        elif continue_playing == 'N':
            return False

#asks user for amount of cards to use
def ask_for_size():
    while True:
        deck_size_input = input('Enter a deck size to use (1-100): ')
        if deck_size_input.isdigit():
            if (1 <= int(deck_size_input) <= 100):
                return int(deck_size_input)

#game loop
def start_game():
    game_continue = True
    while game_continue:
        save_file = open('save.txt', 'r')
        line_list = list(save_file)
        save_file.close()
        if (line_list[0] == 'NO DATA'):
            cards = [number for number in range(ask_for_size())]
            random.shuffle(cards)
            game = Solitaire(cards)
            game.play()
            game_continue = prompt_user()
        else:
            print('******************** SAVED GAME FOUND **************************')
            use_saved_data = prompt_user()
            if use_saved_data == True:
                game = Solitaire([0])
                game.play()
                game_continue = prompt_user()
        clear_save()
    print ('***************** THANK YOU FOR PLAYING ************************')
            

start_game()


