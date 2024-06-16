# for文でループで回す
with open("pep8_introduction.txt") as f:
  for line in f:
      print(line, end="")

# .read()でファイルの中身の全てを一つのstringとして返す
# with open("pep8_introduction.txt") as f:
#    print(f.read())

# この場合f.read()の中身は全てのファイルの中身が含まれているので、重たくなる。

# .readline()で１行ずつ取得してstringで返す
with open("pep8_introduction.txt") as f:
  line = f.readline()
  # line = f.readline()
  print(line)