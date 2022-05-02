def bubble_sort(list):
  # unsorted_until_index : 아직 정렬되지 않은 배열의 가장 오른쪽 인덱스
  # 처음은 전체 배열이 정렬되지 않은 상태이므로 배열의 마지막 인덱스로 변수를 초기화
  unsorted_until_index  = len(list) - 1
  # sorted : 배열의 정렬 여부를 기록
  sorted = False

  # 배열이 정렬될 때까지 계속 실행될 루프
  while not sorted:
    # 교환이 일어나기 전까지 배열이 정렬되어 있다고 가정하고, 값을 교환하면 False로 변경
    # 어떤 교환도 하지 않고 전체 패스스루를 통과할 때 sroted가 True로 남아서 배열이 완전히 정렬된 상태임을 알 수 있다.
    sorted = True

    # 배열 내 모든 값 쌍을 가리킨다.
    # i를 첫 포인터로 사용해 배열의 첫 인덱스부터 아직 정렬되지 않은 인덱스까지 수행한다.
    for i in range(unsorted_until_index):
      # 모든 인접 값 쌍을 비교
      if list[i] > list[i + 1]:
        # 순서가 바뀌어 있으면 교환
        list[i], list[i + 1] = list[i + 1], list[i]
        # 순서를 교환하면 sorted를 False로 바꾼다.
        sorted = False

    # 기존에 가리키고 있던 인덱스가 정렬된 상태이니 1 감소시킨다.
    unsorted_until_index -= 1

  return list

print(bubble_sort([65, 55, 45, 35, 25, 15, 10]))