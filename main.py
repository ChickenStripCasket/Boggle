from pprint import pprint

from generate_board import generate_board
from prefix_tree import PrefixTree
from combinations import Combinations


class Game():
    def __init__(self, size=4):
        self.game_board = generate_board(size)
        pprint(self.game_board)
        self.dictionary = self.get_lines("boggle_dict.txt")
        self.prefix_tree = PrefixTree()
        for word in self.dictionary:
            self.prefix_tree.insert(word)
        self.combination_instance = Combinations(self.game_board, self.prefix_tree)
        self.all_combinations = self.combination_instance.all_searches()
        self.valid_combinations = []

    def get_lines(self, filename="boggle_dict.txt"):
        with open(filename) as file:
            lines = [line.strip() for line in file]
        return lines

    def solve(self):
        for combination in self.all_combinations:
            if self.prefix_tree.contains(combination) is True:
                self.valid_combinations.append(combination)

    def print_solution(self):
        self.solve()
        print(f"{len(self.valid_combinations)} valid combinations: {sorted(self.valid_combinations)}")

def main():
    game = Game()
    game.print_solution()

if __name__ == '__main__':
    main()
