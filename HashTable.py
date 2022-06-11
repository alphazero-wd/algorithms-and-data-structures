from math import isnan

class HashTable:
  def __init__(self, size: int) -> None:
    self.size = size
    self.keys = [None] * size
    self.values = [None] * size
    self.limit = 0
  
  def put_linear_probing(self, key: int, value: int) -> None:
    if self.limit >= self.size: 
      raise Exception('Hash table is full!')
    
    hash_index = self.hash(key)

    while self.keys[hash_index]:
      hash_index += 1
      hash_index %= self.size

    self.keys[hash_index] = key
    self.values[hash_index] = value
    self.limit += 1

  def put_quadratic_probing(self, key: int, value: int) -> None:
    if self.limit >= self.size: 
      raise Exception('Hash table is full!')
    
    hash_index = self.hash(key)
    square_index = 1

    while self.keys[hash_index]:
      hash_index += pow(square_index, 2)
      square_index += 1

      hash_index %= self.size

    self.keys[hash_index] = key
    self.values[hash_index] = value
    self.limit += 1

  def get_linear_probing(self, key: int) -> int:
    hash_index = self.hash(key)
    while self.keys[hash_index] != key:
      hash_index += 1
      hash_index %= self.size
    return self.values[hash_index]

  def get_quadratic_probing(self, key: int) -> int:
    hash_index = self.hash(key)
    square_index = 1
    while self.keys[hash_index] != key:
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