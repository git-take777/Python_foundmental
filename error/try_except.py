def split_bill(price):
  num = input("何人で割り勘しますか")
  try:
    each = price/ int(num)
  except ZeroDivisionError:
    print("エラーが発生しました。")
    each = price
  except ValueError:
    print('数字を入力してください')
  print(f"一人{each}円です")
  if __name__ == "__main__":
    split_bill(10000)