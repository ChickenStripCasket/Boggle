from prefix_tree_node import PrefixTreeNode


class PrefixTree:
    START_CHARACTER = ''

    def __init__(self, strings=None):
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        self.size = 0
        if strings is not None:
            for string in strings:
                self.insert(string)


    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def contains(self, string):
        current_node = self.root
        for letter in string:
            if not current_node.has_child(letter):
                return False
            current_node = current_node.get_child(letter)
        return current_node.terminal

    def insert(self, string):
        current_node = self.root
        for letter in string:
            if current_node.has_child(letter):
                current_node = current_node.get_child(letter)
            else:
                current_node.add_child(letter, PrefixTreeNode(letter))
                current_node = current_node.get_child(letter)
        # Check to make sure string has not already been added
        if current_node.terminal is False:
            self.size += 1
            current_node.terminal = True

    def _find_node(self, string):
        if len(string) == 0:
            return self.root, 0
        current_node = self.root
        depth = 0
        for letter in string:
            if current_node.has_child(letter) is False:
                return None, depth
            current_node = current_node.get_child(letter)
            depth += 1
        return current_node, depth

    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""
        completions = []
        node, _ = self._find_node(prefix)
        if node:
            if node.terminal:
                completions.append(prefix)
            self._traverse(node, prefix, completions.append)
        return completions

    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        all_strings = []
        self._traverse(self.root, "", all_strings.append)
        return all_strings

    def _traverse(self, node, prefix, visit):
        #Traverse this prefix tree with recursive depth-first traversal.
        for child_node in node.children:
            new_prefix = prefix + child_node.character
            if child_node.terminal:
                visit(new_prefix)
            self._traverse(child_node, new_prefix, visit)

def create_prefix_tree(strings):
    tree = PrefixTree()
    for string in strings:
        tree.insert(string)




