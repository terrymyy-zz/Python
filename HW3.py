import random
global deck, discard
deck    =  list(range(1,61))
discard =  list()
             
def shuffle():
    global deck, discard
    if len(deck) == 0:
        random.shuffle(discard)
    else:
        random.shuffle(deck)

def check_racko(rack):
    return sorted(rack, reverse =  True) == rack

def deal_card():
    global deck
    new_card = deck.pop()
    return new_card

def deal_initial_hands():
    global deck
    computer_hand = list()
    user_hand = list()
    for i in range(0,10):
        computer_hand.append(deal_card())
        user_hand.append(deal_card())
    return computer_hand, user_hand

def does_user_begin():
    ''' user begins if 1 pops up, computer begins if 0 pops up'''
    return random.randint(0,1) == 1

def print_top_to_bottom(rack):
    for card in rack:
        print card

def find_and_replace(newCard,cardToBeReplaced,hand):
    global deck, discard
    index = hand.index(cardToBeReplaced) 
    if index in range(0,10):
        hand[index] = newCard
        add_card_to_discard(cardToBeReplaced)
    else:
        print ' Sorry the card you wanna replace is not actually in your hand'
    return hand 

def add_card_to_discard(card):
    global discard
    discard.append(card)

def find_longest_descending_sublist(hand):
    for i in range(1,len(hand)):
        if hand[i] 《 hand [i-1]:
            sub_list.append(hand[i])
        else:



def computer_play(hand):
    global deck,discard


def main():
    global deck,discard
    shuffle()
    computer_hand,use_hand = deal_initial_hands()
    userStarts = does_user_begin()
    print_top_to_bottom(user_hand)
    add_card_to_discard(deck.pop())
    while (not check_racko(user_hand)) and (not check_racko(computer_hand)):
        computer_hand = computer_play(computer_hand)
        user_choice = raw_input('Do you want this card?, y/n \n')
        print_top_to_bottom(user_hand)
        if user_choice == 'y':
            card_to_replace = raw_input('Which card do you wanna replace?\n')
            user_hand = find_and_replace(card,card_to_replace,user_hand)
            print_top_to_bottom(user_hand)
            elif user_choice == 'n':
                card = deck.pop()
                print 'The card you get from the deck is ' + str(card)
                secondChoice = raw_input('Do you wanna keep this card?\n')
                if secondChoice == 'y':
                    card_to_replace = raw_input('Which card do you wanna replace?\n')
                    user_hand = find_and_replace(card,card_to_replace,user_hand)
                else:
                    discard.append(card)
                    print_top_to_bottom(user_hand)
        if len(deck) == 0:
            shuffle()
                    
