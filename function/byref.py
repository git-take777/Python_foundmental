# 参照渡し (byref) <-> 値渡し(byvalue)
# def add_nums(a, b):
#   print(f"第一引数aのID:{id(a)}")
#   print(f"第一引数bのID:{id(b)}")
#   return a + b
# one = 1
# two = 2
# print(f"第一引数oneのID:{id(one)}")
# print(f"第一引数twoのID:{id(two)}")

# print(add_nums(one, two))

# 参照渡しは、値のアドレスを渡す / 値渡しは、その値を渡している

# イミュータブルを使った関数
def add_one(num):
  print(f"変更前のID:{id(num)}")
  num +=1
  print(f"変更後のID:{id(num)}")
  return num

  value = 1
  print(id(value))
  print(f"関数の呼び出し前のvalue:{value}")
  add_one(value)
  print(f"関数呼び出し後のone:{one}")
add_one()
# ニュータブル
def add_fruit(fruits, fruit):
    print(f"変更前のID: {id(fruits)}")
    fruits.append(fruit)
    print(f"変更後のID:{id(fruits)}")
    return fruits
add_fruit()
myfruits = ['apple', 'banana', 'peatch']
myfruit = 'lemon'
print(f"関数呼び出し前のmyfruits:{myfruits}")
add_fruit(myfruits, myfruit)
print(f"関数呼び出し後のmyfruits:{myfruits}")

# 重要:ニュータブルなイメージとイミュータブルのイメージは異なる
# どのタイプの引数を入れたかによって異なる。

