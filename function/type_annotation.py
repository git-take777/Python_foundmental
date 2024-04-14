# Type annotation
def add_nums(num1: int, num2: int) -> int:
  return num1 + num2

# 動的型付け言語・・・値が代入や値が処理されるまで、データ型がわからないことを指す
print(add_nums("1", "2"))