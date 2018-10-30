'''
输入一个三位数于承于随机数比较大小
- 大于程序随机数，则分别输出这个三位数的个十百位
- 如果等于随机数，则提示中奖
- 小于随机数，则将120个字符输入到文本中（每个字符串的长度是12，单独占一行，并且前四个是字母，后8个是数字）
'''
import random


def line():
    # 前四个字母
    connect = ''
    for m in range(4):
        number = random.randrange(97, 123)  # Ascii中小写英文字母编号
        str_s = chr(number)
        connect = str_s + connect

    # 后8个数字
    for m in range(8):
        number = random.randrange(1, 10)
        connect = connect + str(number)

    return connect

# 初始分数
score = 0
num = input("input your number:")
num = int(num)
rand_num = random.randrange(100,1000)
rand_num = int(rand_num)


# 检测输入的是否为纯数字
if num.isdigit() and 100 <= int(num) <= 999:
    num = int(num)
    random_num = int(random_num)
    if int(num) > int(random_num):  # 强制类型转换，输入的函数为字符
        a = num // 100  # 地板除，取整数部分
        b = num % 100 // 10
        c = num % 10
        print("百位：{0},十位： {1}, 个位：{2}".format(a, b, c))

    if int(num) == int(random_num):
        score += 100
        print("今晚吃鸡")

    if int(num) < int(random_num):
        for i in range(10):
            str_line = line()
            print(str_line)
else:
    print("请正确输入")

