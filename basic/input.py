# input関数を使うと、Userの入力した値を取得できる

# age = input('あなたは何歳ですか')
# print("あなたは{}歳です。".format(age))

# Challenge1
# age = int(input('あなたは何歳ですか?'))
# if age > 18 :
#   print('入れるカジノを作成する')
# else :
#   print('カジノ作成できない')

# Challenge2
age = int(input('あなたは何歳ですか?'))
cazino_age = 18
if age > cazino_age :
  print('入れるカジノを作成する')
  game_text = """
              1. ルーレット
              2. ブラックジャック
              3. ポーカー
              """
  game = input(game_text)
  if game == '1' :
    print('あなたはルーレットを選びました')
  elif game == "2" :
    print('あなたはブラックジャックを選ぼました')
  elif game == 3:
    print('あなたはポーカーを選びました')
  else:
  print('あなたは1~3を選びください')
else :
  print('カジノ作成できない')


