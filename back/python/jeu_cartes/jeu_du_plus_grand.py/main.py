from controller import Controller
from models.deck import Deck
from view import View


def main():
    deck = Deck()
    view = View()
    game = Controller(deck, view)
    game.run()


main()