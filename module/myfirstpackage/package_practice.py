import myfirstpackage.module1
import myfirstpackage.module2


myfirstpackage.module1.myfunc()
myfirstpackage.module2.myfunc()

# __init__がないと名前空間パッケージになる。これは、package名が同じであれば、package名.module名で

# いくら module名が異なっていても同じ扱い。

# また、この処理には時間がかかる。