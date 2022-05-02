function BubbleSort(array) {
  // 배열의 요소를 순환
  for (let i = 0; i < array.length; i++) {
    // 배열 요소의 순서가 바뀐 경우
    if (array[i] > array[i + 1]) {
      // 순서를 교환
      [array[i], array[i + 1]] = [array[i + 1], array[i]];

      // 다음 패스스루를 실행한다.
      BubbleSort(array);
    }
  }

  return array;
}

console.log(BubbleSort([4, 3, 5, 2, 7, 9, 6, 8]));
