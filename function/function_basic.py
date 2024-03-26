# 関数

# 華氏から摂氏に変換する
fahrenherit = 72;
# print(celsius)

def fahrenherit_to_celsius(fahrenherit):
  celsius = (fahrenherit - 32) * 5/9
  return celsius

celsius = fahrenherit_to_celsius(fahrenherit)
print(celsius)