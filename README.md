# Trie

## 1. Introduction

A **trie** or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Trie_example.svg/1024px-Trie_example.svg.png" width="30%" />

_A trie for keys "A", "to", "tea", "ted", "ten", "i", "in", and "inn"._

## 2. Implementation

### 1. Initialization

Each node in a trie has two attributes: `children` is a hash map storing the character as the key, the value is the pointer to the next node; `end_of_word` is a boolean value used to indicate whether the current character is actually the end of a word.

```py
class TrieNode:
  def __init__(self):
    self.children = {}
    self.end_of_word = False
```

We also need a class `Trie` that has an attribute `root`, which is the root of a trie and will be set to an empty node.

```py
class Trie:
  def __init__(self):
    self.root = TrieNode()
```

### 2. Insertion

To insert a word `word` into a trie e.g `happy`. We need to start from `root` and check if `h` is in `root.children`. If not, insert `h` node and repeat the process until `y` is inserted. Then we set `end_of_word` of node `y` to `true`.

**Algorithm**:

1. Have a temporary variable `cur` start at `root`.
2. For each `char` in `word`, check if `char` is in `root.children`.
   1. If `char` is not in `cur.children`, set `cur.children[char]` to a new `TrieNode()`
   2. Set `cur` to the `cur.children[char]`
3. Mark `cur.end_of_word` to `true`.

### 3. Search

To search a word `word` into a trie e.g `happy`. We need to start from `root` and check if `h` is in `root.children`. If not, that means that word does not exist. Repeat the process for every other characters in `word`. At the end, check if the last character's `end_of_word` is `true`.

**Algorithm**:

1. Have a temporary variable `cur` start at `root`.
2. For each `char` in `word`, check if `char` is in `root.children`.
   1. If `char` is not in `cur.children`, return `false`
   2. Set `cur` to the `cur.children[char]`
3. Return if `cur.end_of_word` is `true`.

### 4. Check if a trie starts with a `prefix`

We do exactly the same as search, except for this time, we just check every character in `prefix`. At the end, we return `true` as a prefix does not have to necessarily be the end of a word.

**Algorithm**:

1. Have a temporary variable `cur` start at `root`.
2. For each `char` in `word`, check if `char` is in `root.children`.
   1. If `char` is not in `cur.children`, return `false`
   2. Set `cur` to the `cur.children[char]`
3. Return `true`.

## 3. Summary

| Operation     | Time complexity |
| ------------- | :-------------: |
| Insert        |     `O(n)`      |
| Search        |     `O(n)`      |
| Search Prefix |     `O(n)`      |

_`n` is the number of nodes in a trie_
