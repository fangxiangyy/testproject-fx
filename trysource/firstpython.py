
# print("hello world")


# a = 5
# b = 12
# a = a+b
# b = a-b
# a = a-b
# print("a = " + str(a))
# print("b = " + str(b))
#
# a = 5
# b = 12
# a = a^b
# b = a^b
# a = a^b
# print("a = " + str(a))
# print("b = " + str(b))
import random
import sys
#
# a = random.randint(0,100)
# print(a)
#
# a = sys.modules.keys()
# print(a)
#
# """
# a = 1
# b = 1
# """
# a = bin(12)
# '''
# print(a)
# '''
# print(a)

# a = 100
# b = "Hello"
# c = 1.11
# print(type(a))
# print(type(b))
# print(type(c))
# a=1
# def d():
#     global a
#     a = 2
#     print(a)
# if __name__ == "__main__":
#     d()
#     print(a)

# a = 0
# b = 4
# print(a and b )
# print(a or b)
# print(not a )
# print(a>b and a == b)
# print(a<b and a == b)
# print(not a != b )

#元组
# a = (1,2,"hello",[ 3,"ff"],(4,"gg"),{"q":1,"p":2})
# print(a[0:])
#
# print(a[-1]["p"])
# print(a[5])
# # print(a[3][1])
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print("******************************")
# print(a[-1])
# print(a[-2])
# print(a[-3])
# print(a[-4])
# print(a[-5])
# # list
# a = [1,2,"hello",(3,"dd"),[4,"ee"],{"q":1,"p":2}]
# b = [1,2,"hello",(3,"dd"),[4,"ee"]]
# print(a)
# a.append("ff")
# print(a)
# a.insert(2,"gg")
# print(a)
# a.remove(a[4])
# a.remove([4,"ee"])
# a[4]="hh"
# print(a)
# a.extend(b)
# print(a)
# a = a+b
# print(a)

#dictionary 字典
# d = {"a":1,"b":2,"c":"hello"}
# d1 =  {"a":2,"b":3,"c1":"hello1"}
# d["a"] = 3
# d["d"] = (1,2,"dd")
# d["e"] = [1,2,"ee"]
# d["f"] = {"a":1,"b":2}
# del(d["c"])
# d.update(d1)
# print(d)
# def add(a,b,c):
#     d = a+b+c
#     return a,b,c,d
# a,b,c,d= add(1,2,3)
# print(a,b,c)

import sys


# def a1(a,b):
#     return a+b
#
# def a2(c):
#     return c
#
# def calculate(x,y,z):
#     return a1(x,y) - a2(z)
#
# print(calculate(1,3,5))
#
#
# print(sys.path)

# print("a \t")
# print("ab\"c")
# print(r"ab",r"\\r\\n\\t",r"c")
# print("ab","\\")
# print(bin(-1))
# print(10^-9)
import random
import string

#取长度为n的字母和数字的随机字符
from urllib import request


def ran_str(n):
    ran_str=''.join(random.sample(string.ascii_letters+string.digits,n))
    return ran_str

#取长度为n的传入字符串的随机字符 strx='我是方向abcdefj',n=20
def ran_strx(strx,n):
    items = list(strx)
    str2= ''
    for i in range(0,n):
        random.randint(0,len(items)-1)
        str1 = items[random.randint(0,len(items)-1)]
        str2 += str(str1)
    return str2

# print(ran_str(50))
# print(ran_strx('我是方向001',50))


fb = open('t.txt')
# print(fb.readlines())
listfb = fb.readlines()
# print(listfb[0])
list1 = []
list2 = []
for line in listfb:
    # print(line)
    list1 =  line.split('\t')
    # print(list1)
    if(list1[0] == 'a2'):
        # list3 = list1[0].join('\t')
        # list3 = list3.join(list1[4])
        list2.append(list1[4].replace('\n',''))
        # list2.append(list3)
    # print(listfb[line])
# print(list2)
for line3 in list2:
    print(line3)













