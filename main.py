# !/usr/bin/eny python3

from game.game import Game

def main():
    game = Game()
    game.add_small_enemies(10)
    game.run_game()

main()
