// Time complexity: O(k+n)
// Space complexity: O(k)
const countSort = (array) => {
  const hash = {},
    countArr = [];
  for (let val of array) {
    if (!(val in hash)) hash[val] = 1;
    else hash[val]++;
  }

  for (let key in hash) {
    for (let i = 0; i < hash[key]; i++)
      countArr.push(parseInt(key));
  }
  return countArr;
};
