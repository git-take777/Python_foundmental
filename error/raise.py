# raise・・・特定の例外を発生させることができる
try:
  # TODO: 後で削除する
  # 例外インスタンスか
  raise ValueError()
except ValueError:
  # このraiseはvalueErrorの例外を出力するため
  print('Do something')
  # raiseと書くと、exceptの中身を出力し、例外クラスや例外インスタンスのテストができる
  raise