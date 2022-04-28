def linear_search(array, search_value)
  
  # 배열의 모든 원소를 순회
  array.each_with_index do |element, index|
    # print(element, index)

    # 원하는 값을 찾으면 그 인덱스를 반환한다.
    if element == search_value
      return index

    # 찾고 있던 값보다 큰 원소에 도달하면 루프를 일찍 종료할 수 있다.
    elsif element > search_value
      break
    end
  end

  # 배열에서 값을 찾지 못하면 널을 반환한다
  return nil
end

p linear_search([3, 17, 75, 80 ,202], 22) # nil
p linear_search([3, 17, 75, 80 ,202], 17) # 1
p linear_search([3, 17, 75, 80 ,202], 202) # 4

