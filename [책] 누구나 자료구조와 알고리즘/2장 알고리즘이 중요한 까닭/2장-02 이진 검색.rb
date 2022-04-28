def binary_search(array, search_value)
  # 먼저 찾으려는 값이 있을 수 있는 상한선과 하한선을 정한다.
  # 최초의 상한선 : 배열의 첫 번째 값
  lower_bound = 0
  # 최초의 하한선 : 마지막 값
  upper_bound = array.length - 1

  # 상하선과 하한선 사이의 가운데 값을 계속해서 확인하는 루프를 시작한다.
  while lower_bound <= upper_bound do
    # 상한선과 하한선의 중간 지점을 찾는다. (루비는 정수를 나눌 때 결과값을 가장 가까운 정수로 올림한다)
    midpoint = (upper_bound + lower_bound) / 2

    # 중간 지점의 값
    value_at_midpoint = array[midpoint]

    # 중간 지점의 값이 찾을 값이면 검색을 종료
    if search_value == value_at_midpoint
      return midpoint
    # 중간 지점의 값이 찾을 값보다 크면 하한선을 변경
    elsif search_value < value_at_midpoint
      upper_bound = midpoint - 1
    # 중간 지점의 값이 찾을 값보다 작으면 상한선을 변경
    elsif search_value > value_at_midpoint
      lower_bound = midpoint + 1
    end
  end

  # 상한선과 하한선이 같아질 때까지 경계값을 줄였다면, 찾을 값이 이 배열에 없다는 의미
  return nil
end