# whileループ
# リスト要素が終わったらではなく、条件式がTrueの間 回すことができる

while count < 20:
print(count)
count +=1

# breakとcontinue (cotinueは次に進む)
# while True:
#   age = int(input('あなたは何歳ですか?'))
#   if not 0 <= age < 120 :
#     print('入力された値は正しくありません')
#     continue
#   else:
#     print(f"あなたは{age}歳です。")

# Challenge1
# while True:
      age = int(input('あなたは何歳ですか'))
      if (age >= 18) :
        option = """プレイするゲームを選択してください.
        1.ルーレット
        2.ブラックジャック
        3.ポーカー
        :"""
        print(option)
        continue
      else:
        print(f"あなたは{age}のため入れません。")
        break