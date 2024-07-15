import random #importing random module

class BlackJackCard: #class of Card
    def __init__(b,cardsuit,cardrank): #using b instead of self.
        #c resembles card,b resembles blackjack game or self
        b.csuit=cardsuit
        b.crank=cardrank

    def __str__(b): #magic/dunder method
        return (f'{b.crank} of {b.csuit}') #string representation of object before
class BlackJackDeck: #deckLibrary
    def __init__(b):
        b.csuits=['Clubs','Spades','Hearts','Diamonds']
        b.cranks=['J','K','Q','A','2','3','4','5','6','7','8','9']
        b.ccards=[BlackJackCard(csuit,crank) for csuit in b.csuits for crank in b.cranks]

    def BlackJackshuffle(b):
        random.shuffle(b.ccards) #random shuffle of all cards from deck

    def BlackJackdeal(b):
        return b.ccards.pop() #pop:will take from library and removes it.

class BlackJackGame:
    def __init__(b):
        b.bjdeck = BlackJackDeck() #bj resembles blackjack
        b.bjdeck.BlackJackshuffle()
        b.user_hand=[] #player
        b.distributor_hand=[] #dealer
    def deal_first(b):
        for x in range(2): #for the first two cards
            b.user_hand.append(b.bjdeck.BlackJackdeal())
            b.distributor_hand.append(b.bjdeck.BlackJackdeal())
    def Score(b,hand):
        Total_number=0
        If_aces=0 #4 Aces,starts with 0
        for card in hand:
            if card.crank.isdigit():
                Total_number += int(card.crank)
            elif card.crank in ['J', 'Q', 'K']:
                Total_number+=10
            elif card.crank in ['A']:
                Total_number += 11 #'A' is either 11 or 1 depending the condition of the game
                If_aces += 1
        while Total_number > 21 and If_aces:
            Total_number-=10 #maintaing 'A' as 1
            If_aces-=1
            #removing one card
        return Total_number #returning only total number
    def show_hands(b,player_turn=False): #boolean
        print('Your Hand: ',[str(card) for card in b.user_hand], 'Score: ',b.Score(b.user_hand))
        if player_turn:
            print("Computer's Hand: ",str(b.distributor_hand[0])) #will show the one card only
        #else:
            #print("Computer's Hand: ",str(b.distributor_hand[0]),"[Hidden]")
    def BlackJackplay(b):
        b.user_hand=[]
        b.distributor_hand=[]
        b.deal_first()


        while b.Score(b.user_hand)<21:
            b.show_hands(player_turn=True)
            action=input("Do you want to 'hit' or 'stand'?: ").lower() #action will take at lower letter

            if action=='hit':
                b.user_hand.append(b.bjdeck.BlackJackdeal())
            if action == 'stand':
                break
        b.show_hands(player_turn=False)



        while b.Score(b.distributor_hand)<17:
            b.distributor_hand.append(b.bjdeck.BlackJackdeal())

        user_score=b.Score(b.user_hand)
        distributor_score=b.Score(b.distributor_hand)

        #print

        print("Computer's Hand: ",[str(card) for card in b.distributor_hand], "Score: ",b.Score(b.distributor_hand))

        if user_score > 21 or (distributor_score<=21 and distributor_score>user_score):
            print('Dealer Wins!!')
        elif user_score <= 21 and distributor_score<=21 and distributor_score==user_score:
            print('Push(Its a tie)') #meeting every possibility,added this after 5-6 test.
        elif user_score >21 and distributor_score>21 and user_score==distributor_score:
            print('Game is Dismissed') #meeting every possibility,added this after 5-6 test.
        else:
            print('Player wins!!')
if __name__== '__main__': #running as the main program.
    print('''Welcome to BlackJack.
#Rule of Game: You have to get closer to 21 and Greater than your Dealer.
#Rule in Game: You have to write in Keyboard 'hit' to continue run, 'stand' to display the hands.
Enjoy the Game!!''') #a welcome note with rules.
    while True:
        game=BlackJackGame()
        game.BlackJackplay()
        game_again= input('Do you want to play again?(y/n): ').lower() #will take lower capital word
        if game_again != 'y':
            break #done








