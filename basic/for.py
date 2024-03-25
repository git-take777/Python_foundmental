fruits = ['apple', 'peach', 'grapes', 'banana']

# for fruit in fruits :
#   print(f"I love {fruit}!!")

# for char in "Hello World" :
#   print(f"char: {char}")

  # iterationとiterable→イテレーションできるものとできないものある。
  # Challenge1
  # favorite = input("好きなフルーツは?")
  # for fruit in fruits :
  #   if fruit == favorite :
  #     print("I love {}".format(fruit))
  #   else:
  #     print("{}は別に普通...".format(fruit))
  # Charenge2
favorite_fruits = []
normal_fruits = []
for fruit in fruits:
  favorite2 = input(f"{fruit}は好き? y/n")
  if favorite2 == "y" :
      favorite_fruits.append(fruit)
  else:
    normal_fruits.append(fruit)

  print(f"favorite fruits: {favorite_fruits}")
  print(f"normal fruits: {normal_fruits}")