class MyError(Exception):

  def __str__(self):
    return 'My Error occurred'

#Errorをまとめたファイルはimportして呼び出すことを想定するため下記のように記述する
if __name__ == "__main__":
  response = input('y/n?')
  try:
    if response != "y" and response != "n":
      raise MyError
  except MyError as e:
    print(e) #e.__str__()を実行している

  # 自作の例外クラスを作成する場合は特定のファイルにまとめる必要がある