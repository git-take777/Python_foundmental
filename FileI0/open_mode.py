# mode='a': ファイルの最後尾mに内容を追加
# with open('writing_file.txt', mode='a') as f:
#   f.write('mode=a appends text')

# mode='r+': 読み書きどちらも可能
# with open('writing_file.txt', mode="r+") as f:
#   f.write('You can write and read with r+ mode!!')
#   print(f.read())
#   f.write("\nThis should be the last summer")
#   print(f.read())

# mode = 'w+': 読み書きどちらも可能! Truscateされることに注意!!
with open('writing_file.txt', mode='w+') as f:
  # 読み込まれない
  # print(f.read())

  # f.write('You are write and read with w+ mode!!')
  # f.seek(0)
  # print(f.read())

  # mode= 'a+': 読みも書きも可能で,positionが最後尾から始まり,trancatedされる
  with open('writing_file.txt', mode="a+") as f:
    print(f.read())
    f.write("\nYou add senetences to the last of the file content with a+ mode")
    f.seek(0)
    print(f.read())