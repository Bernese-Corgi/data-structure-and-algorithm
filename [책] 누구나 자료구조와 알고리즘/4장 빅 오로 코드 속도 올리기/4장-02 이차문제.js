function hasDuplicateValue(array) {
  let steps = 0;

  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < array.length; j++) {
      steps++; // 단계수 증가

      if (i !== j && array[i] === array[j]) {
        return true;
      }
    }
  }
  console.log(steps); // 중복 값이 있으면 단계수 출력

  return false;
}

hasDuplicateValue([1, 5, 3, 9, 1, 4]); // 아무것도 출력되지 않음
hasDuplicateValue([1, 4, 5, 2, 9]); // 25단계
