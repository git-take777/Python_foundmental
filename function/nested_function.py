# 関数の中で関数を定義する (nested function)
msg = "I am global"
def outer():
  msg = "I am outer"
  def inner():
      # outerのmsgは更新されない→globalじゃないから。
      msg = "I am inner"
      print("This is inner function")
      print(msg)
  inner()
  print(msg)

outer()
print(msg)
# inner　functionは外から見えない状態。呼んでも、意味なし
# inner()