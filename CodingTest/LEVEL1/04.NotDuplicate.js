function notDuplicate(arr) {
  var answer = [];

  answer = arr.reduce((acc, cur, i, arr) => {
    if (arr.indexOf(cur) === i) acc.push(cur);
    return acc;
  }, []);

  return answer;
}

console.log(notDuplicate([1, 1, 3, 3, 0, 1, 1]));
console.log(notDuplicate([4, 4, 4, 3, 3]));
