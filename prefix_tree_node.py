# Full prefix tree node structure has been inspired by Alan Davis - https://github.com/Make-School-Courses/CS-2.1-Trees-Sorting


class PrefixTreeNode:

    CHILDREN_TYPE = list

    def __init__(self, character=None):
        self.character = character
        self.children = PrefixTreeNode.CHILDREN_TYPE()
        self.terminal = False

    def is_terminal(self):
        return self.terminal

    def num_children(self):
        return len(self.children)

    def _index_of_child(self, character):
        for index, child in enumerate(self.children):
            if child.character == character:
                return index
        return None

    def has_child(self, character):
        return self._index_of_child(character) is not None

    def get_child(self, character):
        index = self._index_of_child(character)
        if index is not None:
            return self.children[index]
        else:
            raise ValueError(f'No child exists for character {character!r}')

    def add_child(self, character, child_node):
        if not self.has_child(character):
            self.children.append(child_node)
        else:
            raise ValueError(f'Child exists for character {character!r}')

    def __repr__(self):
        return f'PrefixTreeNode({self.character!r})'

    def __str__(self):
        return f'({self.character})'
