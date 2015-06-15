import random
global deck, discard
deck = list(range(1,61))
discard = list()

def main():
	shuffle()
	computer_hand , human_hand = deal_initial_hands()

	#deal a card to the computer and a card to the user
	#repeat until both have 10 cards
	# userStarts = does_user_begin()
	# print_top_to_bottom(human_hand)
	# #reveal one card to begin the discard pile
	# while neither the computer nor the user has racko:
	# computer_hand = computer_play(computer_hand)
	# #ask the user if they want this card
	# #print the user’s hand
	# if user chooses this card:
	# #ask the user for the number of the card they want to kick out
	# #modify the user’s hand and the discard pile
	# #print the user’s hand
	# elif choice == ’n’:
	# card = deck.pop()
	# print ’The card you get from the deck is ’ + str(card)
	# #ask the user if they want this
	# secondChoice = raw_input(’do you want to keep it?\n’)
	# if secondChoice == ’y’:
	# #modify user’s hand, the discard pile and then print user’s hand
	# else:
	# discard.append(card)
	# #print the user’s hand
	# #check and make sure there are still some cards in the deck
	# #else reshuffle the discard and restart.

def shuffle():
	if len(deck) != 0:
		random.shuffle(deck)
	else:
		random.shuffle(discard)
	pass

def deal_initial_hands():
	computer_hand = list()
    user_hand = list()
	for i in range(10):
		computer_hand.append(deck.pop())
		user_hand.append(deck.pop())
	return computer_hand, user_hand


if __name__ == '__main__':
	main()