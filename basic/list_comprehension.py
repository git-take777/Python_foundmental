# リスト内包表記(list comprehension)

square_list = [] #0,1,4,9.16.25

for i in range(10):
  # 配列に要素を追加する
  square_list.append(i**2)

  print(square_list)

# list comprehension
  square_list = [i **2 for i in range(10)]
  print(square_list)

  even_square_list = [i **2 for i in range(10) if i % 2 == 0]
  print(even_square_list)