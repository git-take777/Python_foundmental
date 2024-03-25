# range (start, stop, step)
# Ex 連番数値を回したい時
# for i in range(3, 10, ) :
#   print(i)

  # Challenge FizzBuzzゲーム
for i in range(1, 51, 1) :
    if(i % 15 == 0) :
      print('FizzBuzz')
    elif(i % 5 == 0) :
      print('Buzz')
    elif (i % 3 ==0) :
      print('Fizz')
    else:
       print(i)