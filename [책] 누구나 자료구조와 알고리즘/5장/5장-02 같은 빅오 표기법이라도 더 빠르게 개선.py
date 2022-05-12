def print_numbers_version_one(upperLimit):
  number = 2

  while number <= upperLimit:
    # number가 짝수면 출력
    if number % 2 == 0:
      print(number)

    number += 1

def print_numbers_version_two(upperLimit):
  number = 2

  while number <= upperLimit:
    print(number)

    # 정의에 따라 다음 짝수로 2씩 증가시킨다.
    number += 2