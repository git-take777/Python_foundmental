with open("writing_file.txt", mode='w') as f:
  # truncatedされる: byte=0に切り詰める→上書きされる
  f.write('You can write contents here\nuse "backslash" to back here')
  f.write("banana")

  # また上記のように「f.write()」を続けて書くと改行なしに書かれる!
# file='f'とすると該当ファイルに書かれる。
  print("You can add a new row using 'file' parameter", file=f, end='\n')
  print('test')