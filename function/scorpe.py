def print_name_local():
  # ローカル変数
  first_name = "Taro"
  last_name = "Yamada"
  print(f"I'm {first_name} {last_name}")

  print_name_local()

  # グローバル変数
  age = 30

  def print_age():
    # 上記のグローバル ageを上書きしたい場合
    global age
    # ローカル変数
    age = 20
    print(f"I 'm {age} years old")

    print_age()
    print(age)