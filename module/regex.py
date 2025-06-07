import re

# Regular Expression (正規表現)

email = "Myemail@gmail.com"
print("@" in email)


# 'myemail@gmailcom'にしてマッチしないと None が返る/ emailにすると、OBJが返る
matched = re.search(r'@\w+\.',email)
print(matched)

if matched:
  print("Matched:", matched.group())
else:
  print("No match found.")

# meteacharacter
# []
print(re.search('[abc]', 'apple'))
print(re.search('[a-c]', 'dpple'))

# ^最初の文字
print(re.search('^[0-9]', '3test0'))

# {n} n回リピート
print(re.search('^[0-9]{4}', '21/3/31'))

# {n,m} n回からm回リピート
print(re.search('^[0-9]{2,4}', '21/3/31'))
#$ 最後の文字
print(re.search('[0-9]{2}$', '2021/3/31'))
# *左のパターンを0回以上繰り返す
print(re.search('a*b', 'aaab'))
# +左のパターンを1回以上繰り返す
print(re.search('a+b', 'aaab'))
# ?左のパターンを0回か1回繰り返す
print(re.search('a?b', 'aaab'))
# | or
print(re.search('abc|012', '01'))
# () グループ化
print(re.search('(ab)+', 'acacac'))

# # 任意の1文字
print(re.search('a.b', 'a1b'))

# \ エスケープ
print(re.search('a\.b', 'a.b'))
# \w[a-zA-Z0-9_] 英数字とアンダースコア
print(re.search(r'\w+', 'abc'))