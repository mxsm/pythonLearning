#!/usr/bin/python3
import keyword

# 基础语法--列出关键字
print(keyword.kwlist)
print("-----------------------------------------")
# 代码之间的缩进
if True:
    print(True)
else:
    print(False)
print("-----------------------------------------")
#缩进不一致
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
print("False")  # 改行会打印出来
print("-----------------------------------------")
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print("False")  # 改行不会打印出来
print("------------------#多行语句-----------------------")
#多行语句
item_1 = 1
item_2 = 2
item_3 = 3
total = item_1 + \
        item_2 + \
        item_3
print( total)
print("-----------------------------------------")
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
print(total[0]);

print("------------------数据类型-----------------------")
plural_1 = 2+3j
plural_2 = 2+3j
print(plural_1*plural_2)
print("------------------数据类型格式化-----------------------")
age = 20;
name = "help"
print('{} was {} years old when he wrote this book'.format(age,name));
