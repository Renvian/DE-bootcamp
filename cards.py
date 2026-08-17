import random
import time

def prime_factors(n):
    prime_factors = []
    for i in range(1,n):
        if n % i == 0:
            prime_factors.append(i)
    return prime_factors

def distribute(deck, players_deck, rounds):
    for i in range(int(rounds)):
        for player_cards in players_deck.values():
            player_cards.append(deck.pop())

def round_play(round, players_deck, players_win):
    print(f"Round {round + 1}: \n")
    for player in players_deck:
        card_index = random.randrange(len(players_deck[player]))
        card = players_deck[player].pop(card_index)
        print(f"{player} :",end = " ")
        time.sleep(1)
        print(f"{card}")
    print("\n")
    while True:
        winner_no = input(f"Enter the player no. of winner (1,{no_of_players}): ")
        winner = "Player " + winner_no
        if winner in players_deck:
            players_win[winner] += 1
            print(f"Congratulations {winner}!! for winning round {round + 1}\n")
            time.sleep(1.5)
            break
        else:
            print("Enter valid player number")


#Welcome Message
print("WELCOME TO THE GAME OF CARDS!!")
print("-" * 25,"\n")

# Deck creation
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
ranks = ["Ace","2","3","4","5","6","7","8","9","10","King","Queen","Jack"]
deck = [suit + " " + rank for suit in suits for rank in ranks]

# Shuffling the deck
random.shuffle(deck)

# Input for number of players
while True:
    try:
        no_of_players = int(input("Enter the number of players: "))
        if no_of_players in prime_factors(len(deck)):
            print("\n")
            break
        else:
            print("Enter valid no of players")

    except ValueError:
        print("Please enter a valid input")


# Initializing players
players_deck = {"Player " + f"{i + 1}" : [] for i in range(no_of_players)}
players_win = {"Player " + f"{i + 1}" : 0 for i in range(no_of_players)}


# Distibuting cards
rounds = len(deck) / no_of_players
distribute(deck, players_deck, rounds)

for round in range(int(rounds)):
    round_play(round, players_deck, players_win)


# Results
max_score = 0
max_scorers = []

for player in players_win:
	if players_win[player] > max_score:
		max_scorers.clear()
		max_score = players_win[player]
		max_scorers.append(player)
	elif players_win[player] == max_score:
		max_scorers.append(player)


print("Results: \n")
for player in players_win:
	print(f"{player} : {players_win[player]}")

print("\n")
	
if len(max_scorers) > 1:
			print("The winners are: ")
			for winner in max_scorers:
				print(winner)
else:
			print("The winner is: ")
			print(max_scorers[0])
			
	
			
