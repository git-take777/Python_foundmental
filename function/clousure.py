# Clousure: クロージャ

# 関数もオブジェクト
def compute_squre(num):
  return num * num

print(compute_squre)

f = compute_squre
print(type(f))
print((10))

function_list = [1, True,  f]
print(function_list[-1](10))

# 関数も引数として渡せる