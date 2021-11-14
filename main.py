import json

from solver import solve
from trie import Trie

def load_dictionary(path):
    with open(path) as f:
        data = json.load(f)
        return data


if __name__ == '__main__':
    dictionary = load_dictionary('assets/dictionary.json')
    trie = Trie()
    for word, meaning in dictionary.items():
        trie.insert(word, meaning)
    matrix = [['a','e', 'f'],['tr','l', 'b'], ['s', 'u', 'er']]
    res = solve(matrix, trie)
    for w, m in res:    
        print(w)

