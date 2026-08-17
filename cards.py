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
        #time.sleep(1)
        print(f"{card}")
    print("\n")
    while True:
        winner_no = input(f"Enter the player no. of winner (1,{no_of_players}): ")
        winner = "Player " + winner_no
        if winner in players_deck:
            players_win[winner] += 1
            print(f"Congratulations {winner}!! for winning {round + 1}\n")
            #time.sleep(1.5)
            break
        else:
            print("Enter valid player number")
        
       
# Deck creation
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
ranks = ["Ace","2","3","4","5","6","7","8","9","10","King","Queen","Jack"]
deck = [suit + " " + rank for suit in suits for rank in ranks]
print(len(deck))

# Shuffling the deck
random.shuffle(deck)
print(prime_factors(len(deck)))
# Input for number of players
while True:
    try:
        no_of_players = int(input("Enter the number of players: "))
        print("\n")
        if no_of_players in prime_factors(len(deck)):
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


#Selection sort
    



