# 関数の引数には　「=」の左右にスペースは入れない。
def greeting() :
  return magic(r = real)
# →✖︎


# カンマの後にとじかっこがある場合は「スペース不要」
# correct
foo = (0,)