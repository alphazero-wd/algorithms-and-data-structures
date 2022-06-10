# AND operator (&):
print(9 & 5) # 1
"""
Explaination: 
  9 in binary is 1001, and 5 in binary is 101.
  9    : 0 1 0 0 1
  5    : 0 0 1 0 1
  9 & 5: 0 0 0 0 1 = 1
"""

print(40 & 41) # 40
"""
Explaination:
  40 in base 10 = 100010 in base 2
  41 in base 10 = 100011 in base 2
  40     : 0 1 0 0 0 1 0
  41     : 0 1 0 0 0 1 1
  40 & 41: 0 1 0 0 0 1 0 = 40
"""

# OR operator (|):
print(9 | 5) # 13
"""
Explaination: 
  9    : 0 1 0 0 1
  5    : 0 0 1 0 1
  9 | 5: 0 1 1 0 1 = 13
"""

print(40 | 41) # 41
"""
Explaination:
  40      : 0 1 0 0 0 1 0
  41      : 0 1 0 0 0 1 1
  40 | 41 : 0 1 0 0 0 1 1 = 41
"""

# XOR operator (^):
print(9 ^ 5) # 12
"""
Explaination: 
  9    : 0 1 0 0 1
  5    : 0 0 1 0 1
  9 ^ 5: 0 1 1 0 0 = 12
"""

print(40 ^ 41) # 1
"""
Explaination: 
  40      : 0 1 0 0 0 1 0
  41      : 0 1 0 0 0 1 1
  40 ^ 41 : 0 0 0 0 0 0 1 = 1
"""

# NOT operator (~):
print(~9) # -10
"""
Explaination:
  9    : 0 1 0 0 1
  ~9   : 1 0 1 1 0 = -10
"""

print(~5) # -6
"""
Explaination:
  5 : 0 1 0 1
  ~5: 1 0 1 0 = -6
"""

# Left Shift Operator (<<):
print(9 << 1) # 18
print(9 << 2) # 36
"""
Explaination:
  9     : 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1
  9 << 1: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 = 18
  9 << 2: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 = 36
"""

# Right Shift Operator (>>):
print(9 >> 1) # 4
"""
Explaination:
  9     : 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1
  9 >> 1: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 = 4
"""

print(-9 >> 2) # -3
"""
Explaination:
  -9     : 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1
  -9 >> 2: 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 = -3
"""

# Zero Fill Right Shift (>>>) NOT SUPPORTED IN PYTHON!
def zero_fill_right_shift(a, b):
  return (a >> b) if a >= 0 else ((a + 0x100000000) >> b)

print(zero_fill_right_shift(-9, 1)) # 2147483643
"""
Explaination:
  -9      : 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1
  -9 >>> 1: 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 = 2147483643
"""
