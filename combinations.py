from generate_board import generate_board

class Combinations():
    def __init__(self, board, prefix_tree):
        self.board = board
        self.prefix_tree = prefix_tree
        self.neighbor_coordinates = [
            (-1,-1),  # Up left
            (-1, 0),  # Up
            (-1, 1),  # Up right
            (0, -1),  # Left
            (0,  1),  # Right
            (1, -1),  # Down left
            (1,  0),  # Down
            (1,  1),  # Down right
        ]
        self.all_combinations = set()
        self.column_length = len(board[0])
        self.row_length = len(board)

    def get_neighbors(self, row_index, column_index):
        all_neighbors = []
        for row_offset, column_offset in self.neighbor_coordinates:
            new_row = row_index + row_offset
            new_column = column_index + column_offset

            if (0 <= new_row < self.row_length and 0 <= new_column < self.column_length):  
                all_neighbors.append((new_row, new_column))
        return all_neighbors

    def depth_first_search(self, row, column, visited_path, current_combination):
       
        letter = self.board[row][column]
        visited_path.append((row, column))

        current_combination += letter
        if self.prefix_tree.contains(current_combination):
            self.all_combinations.add(current_combination)

        completions = self.prefix_tree.complete(current_combination)
        if len(completions) == 0:
            return

        current_neighbors = self.get_neighbors(row, column)
        for neighbor in current_neighbors:
            if neighbor not in visited_path:
                self.depth_first_search(neighbor[0], neighbor[1], visited_path.copy(), current_combination)

    def all_searches(self):

        for row_index in range(self.row_length):
            for column_index in range(self.column_length):
                self.depth_first_search(row_index, column_index, [], "")
        return self.all_combinations