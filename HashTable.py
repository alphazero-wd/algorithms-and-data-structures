from math import isnan

class HashTable:
  def __init__(self, size: int) -> None:
    self.size = size
    self.keys = [None] * size
    self.values = [None] * size
    self.limit = 0

  def put(self, key: int, value: int) -> None:
    if self.limit >= self.size: 
      raise Exception('Hash table is full!')
    
    hash_index = self.hash(key)
    square_index = 1

    while self.keys[hash_index]:
      # Linear Probing
      # UNCOMMENT THIS LINE FOR LINEAR PROBING
      hash_index += 1

      # Quadratic Probing
      # UNCOMMENT 2 LINES BELOW FOR QUADRATIC PROBING
      hash_index += pow(square_index, 2)
      square_index += 1

      hash_index %= self.size

    self.keys[hash_index] = key
    self.values[hash_index] = value
    self.limit += 1

  def get(self, key: int) -> int:
    hash_index = self.hash(key)
    square_index = 1
    while self.keys[hash_index] != key:
      # Linear Probing
      # UNCOMMENT THIS LINE FOR LINEAR PROBING
      hash_index += 1

      # Quadratic Probing
      # UNCOMMENT 2 LINES BELOW FOR QUADRATIC PROBING
      hash_index += pow(square_index, 2)
      square_index += 1

      hash_index %= self.size
    return self.values[hash_index]
  def second_hash(self, hashed_key: int) -> int:
    r = self.size - 2
    return r - hashed_key % r

  def hash(self, key: int) -> int:
    if isnan(key): raise Exception('Key must be an integer!')
    # Double Hashing
    return self.second_hash(key % self.size)

# Time complexity:
# Operation       Average     Worst
# Insertion       O(1)        O(n)
# Lookup          O(1)        O(n) 