# 🌳 What is a Trie (Prefix Tree)?

A **Trie** is a **tree-like data structure** used to efficiently store and search strings, especially useful for prefix-based operations.

## 📌 Motivation

- ✅ List → Linear search time (`O(n)`), slow for lookups.
- ✅ HashMap (`dict`) → Fast word lookup (`O(1)`), but can't efficiently find prefixes.
- ❌ Both struggle with finding **all words that start with a given prefix**.

## 🔠 Definition

- Each node stores **one character**.
- Words are formed by **paths from the root** to leaf/end nodes.
- Nodes have a flag to mark the **end of a valid word**.

## 🧠 Key Concept

- **Shared prefixes** are stored once, saving memory.
- Great for problems involving:
  - Autocomplete
  - Word matching
  - Dictionary filtering

## 🔍 Example: Storing "cat", "cap", "do"

```
      (root)
      /    \
     c      d
     |      |
     a      o*
     |
     t* --- p*
```

- `*` marks the **end of a complete word**
- `"cat"` → `root → c → a → t*`
- `"cap"` → reuse `c → a`, then `→ p*`
- `"do"` → `root → d → o*`

> `'a'` is not marked because `"ca"` is not a word.

## ⚙️ Benefits

- Fast **insert** and **search**: `O(m)` where `m = length of word`
- Efficient **prefix lookup**
- Scales well with large dictionaries that share common prefixes

```python
class TrieNode:
  def __init__(self):
    self.children = {}
    self.isEndWord = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word: str):
    cur = self.root
    for char in word:
      if char not in cur.children:
        cur.children[char] = TrieNode()
      cur = cur.children[char]
    cur.isEndWord = True

  def search(self, word: str) -> bool:
    cur = self.root
    for ch in word:
      if ch not in cur.children:
        return False
      cur = cur.children[ch]
    return cur.isEndWord
  
  def startsWith(self, word: str) -> bool:
    cur = self.root
    for ch in word:
      if ch not in cur.children:
        return False
      cur = cur.children[ch]
    return True
  
  def delete(self, word: str):
    self._delete_rec(self.root, word, 0)
  
  def _delete_rec(self, current_node, word, index):
    if index == len(word):
      if not current_node.isEndWord:
        return False
      
      current_node.isEndWord = False

      return len(current_node.children) == 0
    
    char = word[index]
    if char not in current_node.children:
      return False
    should_delete_child = self._delete_rec(current_node.children[char], word, index + 1)

    if should_delete_child:
      del current_node.children[char]

      return not current_node.isEndWord and len(current_node.children) == 0
    
    return False
```