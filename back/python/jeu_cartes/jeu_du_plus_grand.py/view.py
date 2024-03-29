class View: 
    def prompt_for_player(self):
        name = input("tapz le nom du joueur : ")
        if not name:
            return None
        return name

    def show_player_hand(self, name, hand):
        print(f"[Joueur {name}]")
        for card in hand:
            if card.is_face_up:
                print(card)
            else:
                print("(Carte face cachée)")

    def prompt_for_flip_cards(self):
        print()
        input("Prêt à retourner les cartes ?")
        return True

    def show_winner(self, name):
        print(f"Bravo {name} !")

    def prompt_for_new_game(self):
        print("Souhaitez vous refaire une partie ?")
        choice = input("Y/n: ")
        if choice == "n":
            return False
        return True
