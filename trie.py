from typing import Optional

class TrieNode(object):

    def __init__(self):
        self.children = {}
        self.is_word = False

    def set_word(self, meaning, word):
        """Sets current node as a word and add meaning to it."""
        self.is_word = True
        self.meaning = meaning
        self.word = word

    def add_child(self, ch: str):
        if ch not in self.children:
            child = TrieNode()
            self.children[ch] = child
            child.parent = self
        return self.children[ch]
    
    def move(self, ch: str) -> Optional['TrieNode']:
        """
        Tries to move to a new char at cursor. Return the node if has such a char.
        Return None if unable to move.
        """
        if ch in self.children:
            return self.children[ch]
        return None

    def move_back(self):
        return self.parent


class Trie(object):

    def __init__(self):
        self._root = TrieNode()
        self._cursor = self._root

    def get_root(self):
        return self._root
    def insert(self, word: str, meaning: str):
        curr_node = self._root
        for ch in word:
            curr_node = curr_node.add_child(ch)
        curr_node.set_word(meaning, word)


