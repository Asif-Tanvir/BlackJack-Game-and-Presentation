import unittest #importing module for unit testing
from PythonGame_BlackJack_AsifMohammadTanvir import BlackJackGame,BlackJackCard
#from my main coding i have to import Game and card

class Test_for_Calculation_score(unittest.TestCase): #class for testing
    def test_with_number_cards(self): #doing the test for number cards only
        hand=[BlackJackCard('Clubs','A' ),BlackJackCard('Diamond','A'), BlackJackCard('Hearts','10')] #taking two random cards
        game=BlackJackGame()
        score=game.Score(hand)
        self.assertEqual(score,12) #because 5 and 7 is equal to 12,assertEqual is method for comparing actual and expected score
if __name__ =='__main__':
    unittest.main()

