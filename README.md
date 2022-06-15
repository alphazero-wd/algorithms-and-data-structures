# Bit Manipulation

## 1. AND Operator (`&`)

### 1. Rules

| `a` | `b` | `a & b` |
| :-: | :-: | :-----: |
| `0` | `0` |   `0`   |
| `0` | `1` |   `0`   |
| `1` | `0` |   `0`   |
| `1` | `1` |   `1`   |

### 2. Examples

```py
print(9 & 5) # 1
```

_Explaination_:
| | |
| --- | --- |
| `9` | ` 0 1 0 0 1` |
| `5` | ` 0 0 1 0 1` |
| `9 & 5` | ` 0 0 0 0 1 = 1` |

```py
print(40 & 41) # 40
```

_Explaination_:
| | |
| --- | --- |
| `40` | `0 1 0 0 0 1 0` |
| `41` | `0 1 0 0 0 1 1` |
| `40 & 41` | `0 1 0 0 0 1 0 = 40` |

## 2. OR Operator (`|`)

### 1. Rules

| `a` | `b` | `a \| b` |
| :-: | :-: | :------: |
| `0` | `0` |   `0`    |
| `0` | `1` |   `1`    |
| `1` | `0` |   `1`    |
| `1` | `1` |   `1`    |

### 2. Examples

```py
print(9 | 5) # 13
```

_Explaination_:
| | |
| --- | --- |
| `9` | `0 1 0 0 1` |
| `5` | `0 0 1 0 1` |
| `9 \| 5` | `0 1 1 0 1 = 13` |

```py
print(40 | 41) # 40
```

_Explaination_:
| | |
| --- | --- |
| `40` | `0 1 0 0 0 1 0` |
| `41` | `0 1 0 0 0 1 1` |
| `40 \| 41` | `0 1 0 0 0 1 1 = 41`

## 3. XOR Operator (`^`)

### 1. Rules

| `a` | `b` | `a ^ b` |
| :-: | :-: | :-----: |
| `0` | `0` |   `0`   |
| `0` | `1` |   `1`   |
| `1` | `0` |   `1`   |
| `1` | `1` |   `0`   |

### 2. Examples

```py
print(9 ^ 5) # 12
```

_Explaination_:
| | |
| --- | --- |
| `9` | `0 1 0 0 1` |
| `5` | `0 0 1 0 1` |
| `9 ^ 5` | `0 1 1 0 0 = 12` |

```py
print(40 ^ 41) # 40
```

_Explaination_:
| | |
| --- | --- |
| `40` | `0 1 0 0 0 1 0` |
| `41` | `0 1 0 0 0 1 1` |
| `40 ^ 41` | `0 0 0 0 0 0 1 = 1`

## 4. NOT Operator (`~`)

### 1. Rules

| `a` | `~a` |
| :-: | :--: |
| `0` | `1`  |
| `1` | `0`  |

### 2. Examples

```py
print(~9) # -10
```

_Explaination_:
| | |
| --- | --- |
| `9` | `0 1 0 0 1` |
| `~9` | `1 0 1 1 0 = -10` |

```py
print(~5) # -6
```

_Explaination_:
| | |
| --- | --- |
| `5` | `0 1 0 1` |
| `~5` | `1 0 1 0 = -6`

## 5. Left Shift Operator (`<<`)

### 1. Rule:

In left shift, all the bits are shifted to the left, and any excess bits shifted off to the left are
discarded.

### 2. Examples:

```py
print(9 << 1) # 18
print(9 << 2) # 36
```

_Explaination_:
| | |
| --- | --- |
| `9` | `0 0 1 0 0 1` |
| `9 << 1` | `0 1 0 0 1 0 = 18` |
| `9 << 2` | ` 1 0 0 1 0 0 = 36` |

## 6. Right Shift Operator (`>>`)

### 1. Rule:

In right shift, all the bits are shifted to the right, and any excess bits shifted off to the right are
discarded.

## 2. Example

```py
print(9 >> 1) # 4
```

_Explaination_:
| | |
| --- | --- |
| `9` | `0 0 1 0 0 1` |
| `9 >> 1` | `0 0 0 1 0 0 = 4` |

```py
print(-9 >> 2) # -3
```

_Explaination_:
| | |
| --- | --- |
| `-9` | `1 0 1 1 1` |
| `-9 >> 2` | `1 1 1 0 1 = -3` |

> In some languages such as Javascript, the bitwise operators and shift operators operate on 32-bit ints, and if a number gets too big, it overflows the 32 bit capacity. However, in Python it does not behave like that. If a number gets too big, it will not overflow. Therefore, the result will be different.
> <br> <br>
> Take a look at this code snippet
>
> ```py
> print(1073741833 << 2) # 4294967332
> ```
>
> However, the correct output should be `36` because
>
> |                   |                                                                        |
> | ----------------- | ---------------------------------------------------------------------- |
> | `1073741833`      | `0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1`      |
> | `1073741833 << 2` | `0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 = 36` |
>
> The `1` on the very left of `1073741833` should be discarded after being left shifted by `2`. However, Python prevents that from happening. Therefore, the output is `4294967332`, which is represented in binary as `0100000000000000000000000000100100`. The `1` on the very left has not been discarded.
>
> If we want to achieve the same result, we can `& 0x7FFFFFFF`, which is `2^31 - 1`
>
> ```py
> print((10734741833 << 2) & 0x7FFFFFFF) # 36
> ```
> [Reference (StackOverFlow)](https://stackoverflow.com/questions/41610186/difference-between-javascript-bit-wise-operator-code-and-python-bit-wise-operato)
> <br>
