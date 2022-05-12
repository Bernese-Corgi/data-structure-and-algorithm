# def greatestNumber(array):
#   for i in array:
#     # 우선은 i가 가장 크다고 가정
#     isIValTheGreatest = True

#     for j in array:
#       # i보다 큰 값을 찾으면, i는 가장 큰 수가 아니다.
#       if j > i:
#         isIValTheGreatest = False

#     # 나머지 두 수를 모두 확인했는데도 i가 가장 크면, i가 가장 큰 수이다.
#     if isIValTheGreatest:
#       return i

# print(greatestNumber([3,2,5,7,1,8]))

def greatestNumber(array):
  greatestNumberSoFar = array[0]

  for i in array:
    if i > greatestNumberSoFar:
      greatestNumberSoFar = i

  return greatestNumberSoFar

print(greatestNumber([3,2,5,7,1,8]))