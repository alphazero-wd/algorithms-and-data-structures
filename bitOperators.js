const add = (a, b) => {
  while (b) {
    const carry = a & b;
    a ^= b;
    b = carry << 1;
  }
  return a;
};

const negate = (a) => {
  return addition(~a, 1);
};

const subtract = (a, b) => {
  return add(a, negate(b));
};

const multiply = (a, b) => {
  let m = 1,
    c = 0;
  if (a < 0) {
    a = negate(a);
    b = negate(b);
  }
  while (a >= m && b) {
    if (a & m) {
      c = addition(b, c);
    }
    b = b << 1;
    m = m << 1;
  }
  return c;
};
const divide = (a, b) => {
  let c = 0,
    isNegative = 0;
  if (a < 0) {
    a = negate(a);
    isNegative = !isNegative;
  }
  if (b < 0) {
    b = negate(b);
    isNegative = !isNegative;
  }
  if (b) {
    while (a >= b) {
      a = subtraction(a, b);
      c++;
    }
  }

  if (isNegative) c = negate(c);
  return c;
};
