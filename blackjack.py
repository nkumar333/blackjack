if __name__ == "__main__":
	'''BLACKJACK GAME PLAY. A DECK IS CREATED AND SHUFFLED THEN SPLIT UP INTO TWO LISTS (KEYS ARE ONE LIST AND VALUES ARE ANOTHER).
	AFTER A NEW PLAYER IS CREATED. THEN A NEW DEALER IS CREATED. PLAYER BETS AN AMOUNT. DEALER RECEIVES FIRST HAND THEN PLAYER
	RECEIVES A HAND. PLAYER PLAYS FIRST THEN DEALER. MAIN CODE IS AT THE BOTTOM AFTER ALL CLASS AND FUNCTION DEFINITIONS.'''

	import random	
	
	class Card():
		'''ABSTRACT CLASS FOR SUITED CARDS'''

		def __init__(self):
			'''ABTRACT ATTRIBUTE TO SERVE AS SKELETON FOR CHILD CLASSES'''

			self.card = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10, "Ace":11}

		def my_label(self, card):
			'''ABTRACT METHOD TO SERVE AS SKELETON FOR CHILD CLASSES'''
			return self.card

	class Blackjackmoves():
		'''ABSTRACT CLASS FOR PLAYER AND DEALER CHILD CLASSES'''

		def play(self):
			'''ABTRACT METHOD TO SERVE AS SKELETON FOR CHILD CLASSES'''

			return None

		def startinghand(self):
			'''ABTRACT METHOD TO SERVE AS SKELETON FOR CHILD CLASSES'''

			return None

	class Spades(Card):
		'''THIS CLASS INHERITS CARD ABSTRACT CLASS'''

		def __init__(self):
			Card.__init__(self)

		def my_label(self, card):
			'''THIS INSTANCE METHOD LABELS GENERIC SUIT AS SPADES.'''

			self.spades = {}	
			for x, y in self.card.items():
				x = x + " of spades"
				self.spades.update({x:y})
			return self.spades

		def __str__(self):
			'''STRING SPECIAL METHOD THAT ALLOWS PRINTING OF CLASS OBJECTS'''
	
			return "%s" % self.spades
 
	class Hearts(Card):
		'''THIS CLASS INHERITS CARD ABSTRACT CLASS'''

		def __init__(self):
			Card.__init__(self)
	
		def my_label(self, card):
			'''THIS INSTANCE METHOD LABELS GENERIC SUIT AS HEARTS.'''

			self.hearts = {}
			for x, y in self.card.items():
				x = x + " of hearts"
				self.hearts.update({x:y})
			return self.hearts
 
		def __str__(self):
			'''STRING SPECIAL METHOD THAT ALLOWS PRINTING OF CLASS OBJECTS'''

			return "%s" % self.hearts

	class Clubs(Card):
		'''THIS CLASS INHERITS CARD ABSTRACT CLASS'''

		def __init__(self):
			Card.__init__(self)

		def my_label(self, card):
			'''THIS INSTANCE METHOD LABELS GENERIC SUIT AS CLUBS.'''

			self.clubs = {}
			for x, y in self.card.items():
				x = x + " of clubs"
				self.clubs.update({x:y})
			return self.clubs

		def __str__(self):
			'''STRING SPECIAL METHOD THAT ALLOWS PRINTING OF CLASS OBJECTS'''

			return "%s" % self.clubs
	 
	class Diamonds(Card):
		'''THIS CLASS INHERITS CARD ABSTRACT CLASS'''

		def __init__(self):
			Card.__init__(self)

		def my_label(self, card):
			'''THIS INSTANCE METHOD LABELS GENERIC SUIT AS DIAMONDS.'''

			self.diamonds = {}
			for x, y in self.card.items():
				x = x + " of diamonds"
				self.diamonds.update({x:y})
			return self.diamonds

		def __str__(self):
			'''STRING SPECIAL METHOD THAT ALLOWS PRINTING OF CLASS OBJECTS'''

			return "%s" % self.diamonds

	class Deck():
		'''THIS CLASS CREATES A NEW DECK OBJECT'''

		def __init__(self):
			self.deck = {}
			self.randomdeck = {}
			self.decklength = 0
			self.randomdeckkeys = []
			self.randomdeckvalues = []
			self.new_spades = Spades()
			self.new_hearts = Hearts()
			self.new_clubs = Clubs()
			self.new_diamonds = Diamonds()

		def one_deck(self):
			'''THIS INSTANCE METHOD CREATES A NEW DECK OF CARDS BY AGGREGATING SUIT DICITONARIES INTO ONE AGGREGATED DICTIONARY.'''

			dict1 = self.new_spades.my_label(self.new_spades.card)
			dict2 = self.new_hearts.my_label(self.new_hearts.card)
			dict3 = self.new_clubs.my_label(self.new_clubs.card)
			dict4 = self.new_diamonds.my_label(self.new_diamonds.card)

			self.deck.update(dict1)
			self.deck.update(dict2)
			self.deck.update(dict3)
			self.deck.update(dict4)

			return self.deck

		def deck_randomizer(self, deck):
			'''THIS INSTANCE METHOD RANDOMLY SELECTS A KEY/VALUE PAIR FROM THE DECK DICTIONARY AND STORES IT INTO A NEW DICTIONARY TO
			SIMULATE SHUFFLING OF THE CARD DECK.'''

			self.decklength = len(self.deck)
	
			i = 0
	
			while i < self.decklength:
				x = random.choice(list(self.deck))
				self.randomdeck.update({x:self.deck[x]})
				self.deck.pop(x)
				i = i + 1
	 
			return self.randomdeck

		def random_deck_keys_split(self, randomizeddeck):
			'''THIS INSTANCE METHOD EXTRACTS KEYS FROM THE RANDOMIZED DECK WHICH IS STORED IN A DICTIONARY AND STORES THEM
			INTO A LIST.'''

			for i in randomizeddeck.keys():
				self.randomdeckkeys.append(i)
			return self.randomdeckkeys
	
		def random_deck_values_split(self, randomizeddeck):
			'''THIS INSTANCE METHOD EXTRACTS VALUES FROM THE RANDOMIZED DECK WHICH IS STORED IN A DICTIONARY AND STORES THEM
			INTO A LIST.'''
		
			for i in randomizeddeck.values():
				self.randomdeckvalues.append(i)
			return self.randomdeckvalues
		
		def __str__(self):
			'''STRING SPECIAL METHOD THAT ALLOWS PRINTING OF CLASS OBJECTS'''

			return "%s" % self.randomdeck

	class Player(Blackjackmoves):
		'''THIS CLASS INHERITS THE BLACKJACKMOVES ABSTRACT CLASS ATTRIBUTES AND METHODS AND POLYMORPHS THEM ACCORDINGLY.'''
		
		def __init__(self):
			Blackjackmoves.__init__(self)
			self.playercount = 0
			self.phand = []
			self.currenthandposition = 0
			self.bet = 0
	 
		def playerbet(self, balance):
			'''INSTANCE METHOD THAT ALLOWS PLAYER TO BET. EACH GAME PLAY BALANCE IS CARRIED OVER INTO EACH NEW HAND.'''

			validbet = True
			global PBALANCE
			PBALANCE = balance
			
			print("Your balance is {} \n ".format(PBALANCE))
			self.bet = int(input("How many chips would you like to bet? Please enter in a whole number. \n"))
			while validbet:
				if self.bet > PBALANCE:
					self.bet = int(input("You don't have enough balance. Please bet an amount less than your balance of {}.\n".format(PBALANCE)))
				else:
					PBALANCE = PBALANCE - self.bet
					validbet = False
			print("Your bet is {}\n".format(self.bet))
			print("Your balance is {}\n".format(PBALANCE))

			return None
	 
		def startinghand(self):
			'''INSTANCE METHOD THAT INITIATIES PLAYERS STARTING HAND. BOTH CARDS ARE SHOWN PER NORMAL BLACKJACK PLAY.'''

			global DECKCOUNT
			global PBALANCE
			global PLAYER_ACEOVERCOUNT
			PLAYER_ACEOVERCOUNT = False

			print("PLAYER'S HAND:")
			self.phand.append(RKEYS[DECKCOUNT])
			self.playercount = self.playercount + RVALUES[DECKCOUNT]
			print(self.phand[self.currenthandposition])
			DECKCOUNT = DECKCOUNT + 1
			self.currenthandposition = self.currenthandposition + 1
			self.phand.append(RKEYS[DECKCOUNT])
			self.playercount = self.playercount + RVALUES[DECKCOUNT]
			print(self.phand[self.currenthandposition])
			DECKCOUNT = DECKCOUNT + 1
			self.currenthandposition = self.currenthandposition + 1
			if acecheck(self.phand, self.playercount):
				self.playercount = self.playercount - 10
				PLAYER_ACEOVERCOUNT = True
			else:
				pass
			if self.playercount == 21:
				print("\n ***BLACKJACK! YOU WIN! YOU GET 2X YOUR BET!")
				PBALANCE = PBALANCE + (self.bet*3)
				playerresponse = input("Would you like to play again? Please enter 'Y' or 'N'\n")
				if playerresponse == "Y":
					replay()
				else:
					exit()
			else:
				pass
			return None
	 
		def play(self):
			'''THESE VARIABLES ARE GLOBAL TO BE ABLE TO BE REFERENCED ACROSS CLASSES AND IN REPLAY FUNCTION. THIS INSTANCE METHOD IS PLAYERS
			GAME PLAY. PLAYER HITS UNTIL DESIRED AND CAN EVENTUALLY STAND OR BUST. IF STAND THEN DEALER PLAY IS INITIATED'''

			global DECKCOUNT
			global PCOUNTTRACKER
			global PBET
			global PBALANCE
			global PLAYER_ACEOVERCOUNT
			gameplay = True

			playerchoice = input("Would you like to Hit or Stand? Enter 'h' or 's'\n")

			while gameplay and PLAYER_ACEOVERCOUNT is False:
				'''THE LOOP OF GAME PLAY IF AN ACE IS NOT IN THE DECK.'''

				if playerchoice == "h":
					self.phand.append(RKEYS[DECKCOUNT])
					self.playercount = self.playercount + RVALUES[DECKCOUNT]
					print(self.phand[self.currenthandposition])
					self.currenthandposition = self.currenthandposition + 1
					DECKCOUNT = DECKCOUNT + 1
					if acecheck(self.phand, self.playercount):
						self.playercount = self.playercount - 10
						PLAYER_ACEOVERCOUNT = True
					else:
						pass
					if self.playercount > 21:
						print("\n***YOU BUSTED! DEALER WON!***\n")
						playerresponse = input("Would you like to play again? Please enter 'Y' or 'N'\n")
						if playerresponse == "Y":
							replay()
						else:
							exit()
					else:
						playerchoice = input("Would you like to Hit or Stand? Enter 'h' or 's'\n")
				elif playerchoice == "s":
					print("Player stands. Dealer is playing.\n")
					gameplay = False
					
			while gameplay and PLAYER_ACEOVERCOUNT:
				'''THE LOOP OF GAME PLAY IF AN ACE IS IN THE DECK AND COUNT HAS BEEN ALREADY REDUCED BY 10. THIS ENSURES
					THAT COUNT IS NOT REDUCED BY 10 EVERY TIME COUNT IS ABOVE 21 AND AN ACE IS PRESENT. SHOULD ONLY HAPPEN
					ONCE PER STANDARD BLACKJACK RULES'''

				if playerchoice == "h":
					self.phand.append(RKEYS[DECKCOUNT])
					self.playercount = self.playercount + RVALUES[DECKCOUNT]
					print(self.phand[self.currenthandposition])
					self.currenthandposition = self.currenthandposition + 1
					DECKCOUNT = DECKCOUNT + 1
					if self.playercount > 21:
						print("\n***YOU BUSTED! DEALER WON!***\n")
						playerresponse = input("Would you like to play again? Please enter 'Y' or 'N'\n")
						if playerresponse == "Y":
							replay()
						else:
							exit()
					else:
						playerchoice = input("Would you like to Hit or Stand? Enter 'h' or 's'\n")
				elif playerchoice == "s":
					print("Player stands. Dealer is playing.\n")
					gameplay = False
			
			PCOUNTTRACKER = self.playercount
			PBET = self.bet

			return None

		def __str__(self):
			'''STRING SPECIAL METHOD THAT ALLOWS PRINTING OF CLASS OBJECTS'''
			
			return "%s" % self.playercount
	 
	class Dealer(Player):
		'''THIS CLASS INHERITS THE PLAYER CLASS ATTRIBUTES AND METHODS AND POLYMORPHS THEM ACCORDINGLY.'''

		def __init__(self):
			Player.__init__(self)
			self.dealercount = 0
			self.dhand = []
			self.currenthandposition = 0
	 
		def startinghand(self):
			'''THIS INSTANCE METHOD IS DEALER'S STARTING HAND. FIRST CARD IS HIDDEN PER NORMAL BLACKJACK PLAY.'''

			global DECKCOUNT
			global DEALER_ACEOVERCOUNT
			DEALER_ACEOVERCOUNT = False
			
			print("DEALER'S HAND:")
			self.dhand.append(RKEYS[DECKCOUNT])
			self.dealercount = self.dealercount + RVALUES[DECKCOUNT]
			print("<card hidden>")
			DECKCOUNT = DECKCOUNT + 1
			self.dhand.append(RKEYS[DECKCOUNT])
			self.dealercount = self.dealercount + RVALUES[DECKCOUNT]
			self.currenthandposition = self.currenthandposition + 1
			print(self.dhand[self.currenthandposition])
			DECKCOUNT = DECKCOUNT + 1
			self.currenthandposition = self.currenthandposition + 1
			if acecheck(self.dhand, self.dealercount):
				self.dealercount = self.dealercount - 10
				DEALER_ACEOVERCOUNT = True
			else:
				pass
			return None
	 
		def play(self):
			'''THESE VARIABLES ARE GLOBAL TO BE ABLE TO BE REFERENCED ACROSS CLASSES AND IN REPLAY FUNCTION. THIS INSTANCE METHOD IS DEALERS
			GAME PLAY. DEALER HITS UNTIL CARD VALUE IS AT LEAST 17.'''

			global DECKCOUNT
			global PCOUNTTRACKER
			global PBET
			global PBALANCE
			global DEALER_ACEOVERCOUNT
			gameplay = True

			print("DEALER'S HAND:")
			print(self.dhand[self.currenthandposition-2])
			print(self.dhand[self.currenthandposition-1])

			while gameplay and DEALER_ACEOVERCOUNT is False:
				'''THE LOOP OF GAME PLAY IF AN ACE IS NOT IN THE DECK.'''

				if self.dealercount < 17:
					self.dhand.append(RKEYS[DECKCOUNT])
					self.dealercount = self.dealercount + RVALUES[DECKCOUNT]
					print(self.dhand[self.currenthandposition])
					self.currenthandposition = self.currenthandposition + 1
					DECKCOUNT = DECKCOUNT + 1
					if acecheck(self.dhand, self.dealercount):
						self.dealercount = self.dealercount - 10
						DEALER_ACEOVERCOUNT = True
					else:
						pass
				else:
					if self.dealercount > 21:
						print("\n***YOU WON! DEALER BUSTED!***\n")
						PBALANCE = PBALANCE + (PBET*2)
						playerresponse = input("Would you like to play again? Please enter 'Y' or 'N'\n")
						if playerresponse == "Y":
							replay()
						else:
							exit()
					elif self.dealercount <= 21 and self.dealercount > PCOUNTTRACKER:
						print("\n***DEALER WON!***\n")
						playerresponse = input("Would you like to play again? Please enter 'Y' or 'N'\n")
						if playerresponse == "Y":
							replay()
						else:
							exit()
					elif self.dealercount <= 21 and self.dealercount < PCOUNTTRACKER:
						print("\n***YOU WON!***\n")
						PBALANCE = PBALANCE + (PBET*2)
						playerresponse = input("Would you like to play again? Please enter 'Y' or 'N'\n")
						if playerresponse == "Y":
							replay()
						else:
							exit()
					else:
						print("\n***DRAW!***\n")
						PBALANCE = PBALANCE + PBET
						playerresponse = input("Would you like to play again? Please enter 'Y' or 'N'\n")
						if playerresponse == "Y":
							replay()
						else:
							exit()

			while gameplay and DEALER_ACEOVERCOUNT:
				'''THE LOOP OF GAME PLAY IF AN ACE IS IN THE DECK AND COUNT HAS BEEN ALREADY REDUCED BY 10. THIS ENSURES
					THAT COUNT IS NOT REDUCED BY 10 EVERY TIME COUNT IS ABOVE 21 AND AN ACE IS PRESENT. SHOULD ONLY HAPPEN
					ONCE PER STANDARD BLACKJACK RULES'''

				if self.dealercount < 17:
					self.dhand.append(RKEYS[DECKCOUNT])
					self.dealercount = self.dealercount + RVALUES[DECKCOUNT]		
					print(self.dhand[self.currenthandposition])
					self.currenthandposition = self.currenthandposition + 1
					DECKCOUNT = DECKCOUNT + 1
				else:
					if self.dealercount > 21:
						print("\n***YOU WON! DEALER BUSTED!***\n")
						PBALANCE = PBALANCE + (PBET*2)
						playerresponse = input("Would you like to play again? Please enter 'Y' or 'N'\n")
						if playerresponse == "Y":
							replay()
						else:
							exit()
					elif self.dealercount <= 21 and self.dealercount > PCOUNTTRACKER:
						print("\n***DEALER WON!***\n")
						playerresponse = input("Would you like to play again? Please enter 'Y' or 'N'\n")
						if playerresponse == "Y":
							replay()
						else:
							exit()
					elif self.dealercount <= 21 and self.dealercount < PCOUNTTRACKER:
						print("\n***YOU WON!***\n")
						PBALANCE = PBALANCE + (PBET*2)
						playerresponse = input("Would you like to play again? Please enter 'Y' or 'N'\n")
						if playerresponse == "Y":
							replay()
						else:
							exit()
					else:
						print("\n***DRAW!***\n")
						PBALANCE = PBALANCE + PBET
						playerresponse = input("Would you like to play again? Please enter 'Y' or 'N'\n")
						if playerresponse == "Y":
							replay()
						else:
							exit()
			return None

		def __str__(self):
			'''STRING SPECIAL METHOD THAT ALLOWS PRINTING OF CLASS OBJECTS'''
			
			return "%s" % self.dealercount
	 
	def acecheck(hand, count):
		'''THE FUNCTION CHECKS TO SEE IF THE WORD 'ACE' IS IN A LIST. IF CARD COUNT IS > 21 AND AN ACE IS IN THE HAND,
		ACE VALUE IS REDUCED FROM 11 TO 1, PER STANDARD BLACKJACK RULES.'''

		if any("Ace" in item for item in hand) and count > 21:
			return True

	def replay():
		'''THE FUNCTION ALLOWS PLAYERS TO REPLAY BLACKJACK. THIS CLEARS COUNTS AND HANDS AND FEEDS IN PLAYER'S LATEST BALANCE
		BASED ON PRIOR GAME PLAY WINNINGS. IF A USER RUNS OUT OF MONEY, HE/SHE CAN CASH IN MORE. COUNTS AND HANDS ARE CLEAR TO
		ENSURE ACE CHECK LOGIC IS INTACT.'''
		
		global PBALANCE
		print("Welcome to BlackJack! Get as close to 21 as you can without going over! \n Dealer hits until she reaches 17. Aces count as 1 or 11.\n")
		NEWPLAYER.playercount = 0
		NEWPLAYER.phand = []
		NEWPLAYER.currenthandposition = 0
		NEWDEALER.dealercount = 0
		NEWDEALER.dhand = []
		NEWDEALER.currenthandposition = 0
		if PBALANCE == 0:
			PBALANCE = int(input("\nYou are all out of money. You need to deposit more cash. How much would you like to play with?\n"))
		else:
			pass
		NEWPLAYER.playerbet(PBALANCE)
		NEWDEALER.startinghand()
		print("\n")
		NEWPLAYER.startinghand()
		print("\n")
		NEWPLAYER.play()
		NEWDEALER.play()
		return None

	
	###MAIN BLACKJACK GAME PLAY	
	DECKCOUNT = 0
	print("Welcome to BlackJack! Get as close to 21 as you can without going over! \n Dealer hits until she reaches 17. Aces count as 1 or 11.\n")
	NEWDECK = Deck()
	RANDOMIZED_DECK = NEWDECK.deck_randomizer(NEWDECK.one_deck())
	RKEYS = NEWDECK.random_deck_keys_split(RANDOMIZED_DECK)
	RVALUES = NEWDECK.random_deck_values_split(RANDOMIZED_DECK)
	NEWPLAYER = Player()
	NEWDEALER = Dealer()
	NEWPLAYER.playerbet(100)
	NEWDEALER.startinghand()
	print("\n")
	NEWPLAYER.startinghand()
	print("\n")
	NEWPLAYER.play()
	NEWDEALER.play()
else:
	print("file is being imported into another module and not the original file.")

