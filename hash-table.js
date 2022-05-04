class HashTable {
  constructor(size) {
    this.size = size;
    this.keys = new Array(size);
    this.values = new Array(size);
    this.limit = 0;
  }

  // Average: O(1)
  // Worst: O(n)
  put(key, value) {
    if (this.limit + 1 > this.size) throw "hash table is full";
    let hashIndex = this.hash(key);
    let squareIndex = 1;

    // Linear probing
    while (this.keys[hashIndex] != null) {
      hashIndex++;
      hashIndex %= this.size;
    }

    // Quadratic Probing
    while (this.keys[hashIndex] != null) {
      hashIndex += Math.pow(squareIndex, 2);
      hashIndex %= this.size;
      squareIndex++;
    }

    this.keys[hashIndex] = key;
    this.values[hashIndex] = value;
    this.limit++;
  }

  hash(key) {
    if (!Number.isInteger(key)) throw "must be int";
    return this.secondHash(key % this.size);
  }

  // Double Hashing
  secondHash(hashKey) {
    const remainder = this.size - 2;
    return remainder - (hashKey % remainder);
  }

  // Average: O(1)
  // Worst: O(n)
  get(key) {
    let hashIndex = this.hash(key);
    let squareIndex = 1;

    // Linear Probing
    while (this.keys[hashIndex] != key) {
      hashIndex++;
      hashIndex %= this.size;
    }

    // Quadratic Probing
    while (this.keys[hashIndex] != null) {
      hashIndex += Math.pow(squareIndex, 2);
      hashIndex %= this.size;
      squareIndex++;
    }

    return this.values[hashIndex];
  }
}
