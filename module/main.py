# __main__
import mymodule
mymoduke.myfunc()

# __name__

# importすると、importしたモジュールの中にあるコードが実行される。よってPythonはどのプログラムを実行するかを分けるために
# __name__にimportで呼ばれたモジュールを代入する

if __name__ == "__main__":
    print("This script is being run directly.")