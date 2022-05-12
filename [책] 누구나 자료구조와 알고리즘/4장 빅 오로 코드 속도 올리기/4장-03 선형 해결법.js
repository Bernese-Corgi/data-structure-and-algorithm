function hasDuplicateValue(array) {
  let steps = 0;
  let existingNumbers = [];

  for (let i = 0; i < array.length; i++) {
    steps++;
    if (existingNumbers[array[i]] === 1) {
      return true;
    } else {
      existingNumbers[array[i]] = 1;
    }
  }
  console.log(steps);

  return false;
}

hasDuplicateValue([1, 5, 3, 9, 1, 4]); // 아무것도 출력되지 않음
hasDuplicateValue([1, 4, 5, 2, 9]); // 5단계
