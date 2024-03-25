# fruits =['apple', 'peach', 'grapes', 'banana']

# for fruit in fruits:
#   choice = input(f"あなたが探しているフルーツは{fruit}ですか? y/n:")
#   if choice == "y":
#     print('見つかって良かったですね')
#     break
#   else:
#     print("そうですか")
# else:
#   print("お探しのフルーツは見当たりませんでした")

# while else
# count = 0
# while count < 10:
#   print(count)
#   count +=1
# else:
#   print("countは10未満ではなくなりました")

balance = 1000
game_price = 200
while balance > game_price:
  choice = input(f"{game_price}円のゲームに参加しますか？(残高:{balance}円)（y/n?):")
  if choice == "y":
    balance -= game_price
    print("それではゲームに参加します、コインを入れてください")
  elif choice == "n":
    print("またあそぼ")
    break
else:
  print(f"あなたは残金100円未満なためゲーム人参加できません")