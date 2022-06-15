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

```js
console.log(9 & 5); // 1
```

_Explaination_:
| | |
| --- | --- |
| `9` | ` 0 1 0 0 1` |
| `5` | ` 0 0 1 0 1` |
| `9 & 5` | ` 0 0 0 0 1 = 1` |

```js
console.log(40 & 41); // 40
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

```js
console.log(9 | 5); // 13
```

_Explaination_:
| | |
| --- | --- |
| `9` | `0 1 0 0 1` |
| `5` | `0 0 1 0 1` |
| `9 \| 5` | `0 1 1 0 1 = 13` |

```js
console.log(40 | 41); // 40
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

```js
console.log(9 ^ 5); // 12
```

_Explaination_:
| | |
| --- | --- |
| `9` | `0 1 0 0 1` |
| `5` | `0 0 1 0 1` |
| `9 ^ 5` | `0 1 1 0 0 = 12` |

```js
console.log(40 ^ 41); // 40
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

```js
console.log(~9); // -10
```

_Explaination_:
| | |
| --- | --- |
| `9` | `0 1 0 0 1` |
| `~9` | `1 0 1 1 0 = -10` |

```js
console.log(~5); // -6
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

```js
console.log(9 << 1); // 18
console.log(9 << 2); // 36
```

_Explaination_:
| | |
| --- | --- |
| `9` | `0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1` |
| `9 << 1` | `0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 = 18` |
| `9 << 2` | `0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 = 36` |

## 6. Right Shift Operator (`>>`)

### 1. Rule:

In right shift, all the bits are shifted to the right, and any excess bits shifted off to the right are
discarded.

## 2. Example

```js
console.log(9 >> 1); // 4
```

_Explaination_:
| | |
| --- | --- |
| `9` | `0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1` |
| `9 >> 1` | `0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 = 4` |

```js
console.log(-9 >> 2); // -3
```

_Explaination_:
| | |
| --- | --- |
| `-9` | `1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1` |
| `-9 >> 2` | `1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 = -3` |

## 7. Number Operators using Bitwise Operators

### 1. Addition

> Given two integers `a` and `b`. Write a function that returns the sum of `a` and `b` without using `+` operator.

**Algorithm**:

1. Compute `carry` by `a & b`
2. XOR `a` with `b`
3. Set `b` to the left shift of `carry` by 1
4. Repeat step 1 to 3 until `b = 0`
5. Return `a` as the sum of `a` and `b`

```js
const add = (a, b) => {
  while (b) {
    const carry = a & b;
    a ^= b;
    b = carry << 1;
  }
  return a;
};
```
