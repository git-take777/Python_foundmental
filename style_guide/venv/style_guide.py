# 変数定義
# correct
x = 1
y = 2

# wrong
xxxxx        = 1
yyyyy        =1
x = 1


# 関数の引数には　「=」の左右にスペースは入れない。
def greeting(a=1, real) :
  return magic(r = real)

# wrong
def greeting(real, a = 1):
  return magic(r = real, i = imga)

# operatorの周りにスペース1個
x = x + 1
x += 1
x = x*2 -1
x = x*x - y*y

# wrong
x = x+1
x + = 1
x = x * 2 - 1
x = x * x - y * y

# カンマの後にとじかっこがある場合は「スペース不要」
# correct
foo = (0,)

# wrong
foo = (0, )

# Files
# correct→「,」をつけよう
Files = [
  xxx.py,
  yyyy.py,
]