import  math
import  numpy as  np
number = 23
guess = 2

if guess == number:
    # 新块从这里开始
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # 新块在这里结束
elif guess < number:
    # 另一代码块
    print('No, it is a little higher than that')
    # 你可以在此做任何你希望在该代码块内进行的事情
else:
    print('No, it is a little lower than that')
    # 你必须通过猜测一个大于（>）设置数的数字来到达这里。

print('Done')

a = np.array([[1,  2],  [3,  4]])

#for
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w)
for w in  words[:]:
    print(w)

for nu in range(10,50,6):
    print(nu)