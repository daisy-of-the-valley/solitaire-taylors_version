#Solitaire (Taylor's Version) •. ° .♫  ♪.• . .

import time
import random

class CardPile:
    def __init__(self):
        #first item will be top of pile, last will be bottom card
        self.items = []

        #card outline template
        self.top = "┌─────˚.*·˚─┐"
        self.middle = f"│{' ' * 11}│"
        self.bottom = "└─˚.*·˚─────┘"
        

    def add_top(self, item):
        #add card to front of the list
        self.items.insert(0, item)

    def add_bottom(self, item):
        #add card to the back of the list
        self.items.append(item)

    def remove_top(self):
        #remove and return first element
        removed_item = self.items.pop(0)
        return removed_item

    def remove_bottom(self):
        #remove and return last element 
        removed_item = self.items.pop()
        return removed_item

    def size(self):
        #return size of self.items
        return len(self.items)

    def peek_top(self):
        #return first element
        return self.items[0]

    def peek_bottom(self):
        #return last element
        return self.items[self.size()-1]

    def print_all(self, index):
        if len(self.items) == 0:
            print(f"Pile {index}: ")  
        elif index == 0:
            first_card_space = 11 - len(self.items[0])
            head_padding = first_card_space // 2
            tail_padding = first_card_space - head_padding
            print(f"{' ' * 7}{(self.top) * len(self.items)}")
            print(f"Pile {index}:│{' ' * head_padding}{self.items[0]}{' ' * tail_padding}│", end="")
            print(f"{self.middle * (len(self.items)-1)}")
            print(f"{' ' * 7}{self.bottom * (len(self.items))}")
        else:
            print(f"{' ' * 7}{(self.top) * len(self.items)}")
            print("Pile " + str(index) + ":", end="")
            for i in range(len(self.items)):
                item_space = 11 - len(self.items[i])
                head_padding = item_space // 2
                tail_padding = item_space - head_padding
                print(f"│{' ' * head_padding}{self.items[i]}{' ' * tail_padding}│", end="")
            print("\n" + f"{' ' * 7}{self.bottom * (len(self.items))}")
    
    def is_valid_move(self, other, order):
        #implemented in Solitaire class
        #returns boolean checking if the index of the card before is one more than the quantity of the given card 
        moving_card = self.peek_top()
        destination_card = other.peek_bottom()
        if order == "A":
            cards_list = TaylorSwiftCards().get_cards()
            cards_list.reverse()
        elif order == "D":
            cards_list = TaylorSwiftCards().get_cards()
        destination_card_index = cards_list.index(destination_card)
        moving_card_index = cards_list.index(moving_card)
        if (destination_card_index - 1) == moving_card_index:
            return True
        return False


class Solitaire:
    def __init__(self, cards, order):
        self.cards = cards
        self.order = order
        self.piles = []
        self.num_cards = len(cards)
        self.num_piles = (self.num_cards // 8) + 3
        self.max_num_moves = (self.num_cards * 2)
        for i in range(self.num_piles):
            self.piles.append(CardPile())
        for i in range(self.num_cards):
            self.piles[0].add_bottom(cards[i])

        #initialising a timer
        self.start_time = None
        self.time_elapsed = 0
        

    def get_pile(self, i):
        return self.piles[i]

    def display(self):
        for i in range(self.num_piles):
            self.piles[i].print_all(i)

    def move(self, p1, p2):
        first_pile = self.get_pile(p1)
        second_pile = self.get_pile(p2)

        #case 1
        if p1 == 0 and p2 == 0:
            if first_pile.size() > 0:
                top_element = first_pile.remove_top()
                first_pile.add_bottom(top_element)
        #case 2
        elif p1 == 0 and p2 > 0 and first_pile.size() > 0:
            if second_pile.size() == 0 or first_pile.is_valid_move(second_pile, self.order): 
                top_element = first_pile.remove_top()
                second_pile.add_bottom(top_element)

        #case 3
        elif p1 > 0 and p2 > 0 and first_pile.size() > 0 and second_pile.size() > 0 and first_pile.is_valid_move(second_pile, self.order):
            for card in range(first_pile.size()):
                top_element = first_pile.remove_top()
                second_pile.add_bottom(top_element)


    def is_complete(self):
        #checks to see if player can win
        first_pile = self.get_pile(0)
        all_cards_other_pile = False

        #iterating through all the piles
        for pile_num in range(1, self.num_piles):
            current_pile = self.get_pile(pile_num)

            #checking to see if current pile has all the cards
            if current_pile.size() != 0 and current_pile.size() == self.num_cards:
                all_cards_other_pile = True

        #checking to see if first pile is empty and all the cards are on one of the other piles
        if first_pile.size() == 0 and all_cards_other_pile:
            return True
        return False


    def play(self):
        move_number = 1
        self.start_time = time.time()
        
        while move_number <= self.max_num_moves and not self.is_complete():
            self.display()
            print()
            print()
            print("{:^150}".format(f"~ Round {move_number} out of {self.max_num_moves} ~"))
            row1 = input("Move from row no.: ")

            #Handling invalid inputs
            while not row1.isdigit():
                #checking to see if player entered "T" or "t", triggering timer
                if row1 == "T" or row1 == "t":
                    current_time = time.time()
                    self.time_elapsed = current_time - self.start_time
                    self.print_timer_block()
                    row1 = input("Move from row no.: ")
                else:
                    print("Invalid input. You must enter an integer or 'T'/'t'.")
                    row1 = input("Please try again: ")

            
            row2 = input("Move to row no.: ")

            #Handling invalid inputs
            while not row2.isdigit():
                #checking to see if player entered "T" or "t", triggering timer in the second input space
                if row2 == "T" or row2 == "t":
                    current_time = time.time()
                    self.time_elapsed = current_time - self.start_time
                    self.print_timer_block()
                    row2 = input("Move to row no.: ")
                else:
                    print("Invalid input. You must enter an integer or 'T'/'t'.")
                    row2 = input("Please try again: ")


            row1 = int(row1)
            row2 = int(row2)
                
            if row1 >= 0 and row2 >= 0 and row1 < self.num_piles and row2 < self.num_piles:
                self.move(row1, row2)
            move_number += 1

            #updating timer
            current_time = time.time()
            self.time_elapsed = current_time - self.start_time

        if self.is_complete():
            print("You Win!")
            self.print_time_taken_to_win()
            print(f" and {move_number - 1} steps.")
            self.display()
        else:
            print("You Lose!")
            print("Better luck next time! ;D")
            more_info = input("Do you want to learn more about when these Taylor Swift albums were released? (Yes/No): ")
            if more_info == "Yes" or more_info == "yes":
                card_deck = TaylorSwiftCards().get_info()


    def print_timer_block(self):
        #getting hours, minutes and seconds 
        hours, remainder = divmod(int(self.time_elapsed), 3600)
        minutes, seconds = divmod(remainder, 60)

        #printing a block to represent the timer
        print()
        print("{:^150}".format("❤"))
        print("{:^150}".format("♪♫•*¨*•.¸¸   Time   ¸¸.•*¨*•♫♪"))
        print("{:^150}".format(f"{hours:02}:{minutes:02}:{seconds:02}"))
        print()


    def print_time_taken_to_win(self):
        #getting hours, minutes and seconds
        hours, remainder = divmod(int(self.time_elapsed), 3600)
        minutes, seconds = divmod(remainder, 60)

        print_hour = hours > 0
        print_minutes = minutes > 0

        #took less than a minute to complete game
        if not print_hour and not print_minutes:
            print(f"You completed the game in {seconds} seconds", end="")
        #took less than an hour to complete game
        elif not print_hour and print_minutes:
            if minutes > 1:
                print(f"You completed the game in {minutes} minutes and {seconds} seconds", end="")
            else:
                print(f"You completed the game in {minutes} minute and {seconds} seconds", end="")
        #took more than an hour to complete game
        else:
            print(f"You completed the game in {hours} hour, {minutes} minutes and {seconds} seconds", end="")

        
        


class TaylorSwiftCards:
    def __init__(self):
        #initialising the card deck with Taylor Swift albums - plays in descending order
        self.cards = ["Debut", "Fearless", "Speak Now", "Red", "1989",
                      "Reputation", "Lover", "Folklore", "Evermore", "Midnights"]
        #index corresponds to relative release year (which was released first)
        self.release_year = [2006, 2008, 2010, 2012, 2014, 2017, 2019, 2020, 2020, 2022]

    def get_cards(self):
        return self.cards

    def get_reverse(self):
        #This is ascending order of cards
        return self.cards.reverse()

    def shuffle(self):
        #randomly shuffles cards
        shuffled = []
        while len(shuffled) != len(self.cards):
            i = random.randint(0, len(self.cards) - 1)
            card = self.cards[i]
            if card not in shuffled:
                shuffled.append(card)
        return shuffled

    def get_info(self):
        #prints info about albums and release years when implemented
        print()
        print("{:^150}".format("─── ♫ ─── ♪ ─── ♫ ♪ ─── ♪ ─── ♫ ─── ♪ ─── ♫ ♪ ───"))
        for i in range(len(self.cards)):
            album, release_year = self.cards[i], self.release_year[i]
            print("{:^150}".format(f"{album} was released in {release_year}."))
            time.sleep(0.1)
        print("{:^150}".format("─── ♫ ─── ♪ ─── ♫ ♪ ─── ♪ ─── ♫ ─── ♪ ─── ♫ ♪ ───"))
        print()


class Menu:
    def __init__(self):
        self.intro_line = ".　 . • ☆ •. ° . ° .• °:. *₊ ﾟ⋆ *･ﾟ° . ☆ •. ° . ° .• °:. *₊  . ° ₊* ° • .:° •. ° . ☆ • ⋆ *･ﾟ･ • °:. *₊ﾟ . •. *･°　• . . ☆ • ⋆ . ° .• °:. *₊ ﾟ*₊• . ."
        self.title = "~ Solitaire (Taylor's Version) ~"
        self.border = "─── ♫ ─── ♪ ─── ♫ ♪ ─── ♪ ─── ♫ ─── ♪ ─── ♫ ♪ ───" * 3
        
    def print_introduction(self):
        print()
        for char in self.intro_line[:len(self.intro_line) - 1]:
            print(char, end='')
            time.sleep(0.001)
        print(self.intro_line[-1])
        print()
        time.sleep(0.4)
        print("{:^150}".format(self.title))
        print()
        time.sleep(0.9)
        print("{:^150}".format("This is a Taylor Swiftified version of the classic game solitaire. Hope you have fun playing :D"))
        print()
        time.sleep(0.6)
        for char in self.intro_line[:len(self.intro_line) - 1]:
            print(char, end='')
            time.sleep(0.001)
        print(self.intro_line[-1])
        print()

    def print_instructions(self):
        print("{:^150}".format("~ Instructions ~"))
        print()
        time.sleep(1)
        print("🌟 You will get a pile of cards with Taylor Swift album names.")
        time.sleep(0.6)
        print("🌟 Your goal is to place these albums in order by release date (ascending or descending - you choose!).")
        time.sleep(0.6)
        print("🌟 You will be asked to enter two numbers - these correspond to pile numbers.")
        time.sleep(0.6)
        print("🌟 The first number is the pile you want to move the card(s) from.")
        time.sleep(0.6)
        print("🌟 The second is the pile you want to move the cards to.")
        time.sleep(0.6)
        print("🌟 Only the first card in Pile 0 is revealed to you, and the rest will be revealed as you move the cards onto other piles.")
        time.sleep(0.6)
        print("🌟 Additionally, if you want to move the first card from the front to the pack of Pile 0, enter 0 for both prompts.")
        time.sleep(0.6)
        print("🌟 Finally, there is a timer ticking away! If you complete the game successfully, the time you took to complete the game will be revealed.")
        time.sleep(0.6)
        print("🌟 If you wish to check the time at any point while playing, simply enter a 'T' or 't' into the prompts. This will not count as a move.")
        time.sleep(0.6)
        print()
        print("{:^150}".format("Happy Playing ✨"))
        print()
        time.sleep(0.85)
        print(self.border)
        print()

    def print_outro(self):
        print()
        for char in self.intro_line[:len(self.intro_line) - 1]:
            print(char, end='')
            time.sleep(0.001)
        print(self.intro_line[-1])
        print()
        print("{:^150}".format("~ Thank you for playing! ~"))
        print()
        print()
        for char in self.intro_line[:len(self.intro_line)]:
            print(char, end='')
            time.sleep(0.001)
        print()
        

def main():
    print("{:^150}".format("*Note: It is recommended that you play with the shell in full screen :)"))
    print()
    menu = Menu()
    menu.print_introduction()
    print()
    time.sleep(0.45)
    menu.print_instructions()
    order = input("Enter 'A' if you want to play it in ascending order (first-released to latest album) or 'D' if you want to play it in descending order: ")
    if order == "A" or order == "D":
        card_deck = TaylorSwiftCards()
        cards = card_deck.shuffle()
    else:
        while order != "A" and order != "D":
            print("Please only enter 'A' or 'D'!")
            order = input("Enter 'A' if you want to play it in ascending order (first-released to latest album) or 'D' if you want to play it in descending order: ")     
        card_deck = TaylorSwiftCards()
        cards = card_deck.shuffle()
    Solitaire(cards, order).play()
    again = input("Do you want to play another round?(Yes/No): ")
    while again == "Yes" or again == "yes":
        print("─── ♫ ─── ♪ ─── ♫ ♪ ─── ♪ ─── ♫ ─── ♪ ─── ♫ ♪ ───" * 3)
        order = input("Enter 'A' if you want to play it in ascending order (first-released to latest album) or 'D' if you want to play it in descending order: ")
        if order == "A" or order == "D":
            card_deck = TaylorSwiftCards()
            cards = card_deck.shuffle()  
        else:
            print("Please only enter 'A' or 'D'!")
            while order != "A" or order != "D":
                order = input("Enter 'A' if you want to play it in ascending order (first-released to latest album) or 'D' if you want to play it in descending order: ") 
        Solitaire(cards, order).play()
    menu.print_outro()
        

main()       

