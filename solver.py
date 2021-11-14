from typing import Set, List, Tuple, Optional
from trie import Trie, TrieNode

DIRS = [
        [[-1, -1], [-1, 0], [-1, 1]],
        [[0, -1],          [0, 1]],
        [[1, -1], [1, 0], [1, 1]],
    ]

def solve(matrix: List[List[str]], trie: Trie) -> List[Tuple[str, str]]:
    res = set()
    R, C = len(matrix), len(matrix[0])
    visited = [[False] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            try_solve(matrix, visited, (r, c), trie.get_root(), res)
    return res

def try_solve(
        matrix: List[List[str]], 
        visited: List[List[bool]],
        loc: Tuple[int, int],
        node: TrieNode,
        res: Set[str]
    ):
    R, C = len(matrix), len(matrix[0])
    r, c = loc
    visited[r][c] = True
    s = matrix[r][c]
    curr_node = node
    for ch in s:
        if not curr_node:
            break
        curr_node = curr_node.move(ch)
    if not curr_node:
        visited[r][c] = False
        return
    if curr_node.is_word and len(curr_node.word) >= 4:
        res.add((curr_node.word, curr_node.meaning))
    for row in DIRS:
        for dr, dc in row:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                try_solve(matrix, visited, (nr, nc), curr_node, res)
    visited[r][c] = False






