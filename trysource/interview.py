#coding:utf-8
import random
import time

from  business.MysqlHelper  import MysqlHelper as MysqlHelper

from  trysource.firstpython import  ran_strx
def qishu(array):
    n = len(array)
    r=['']
    c=r*n*2
    i=0#奇数位
    j=1#偶数位
    for h in array:
        if h%2 == 0  :
            c[j]=h
            j+=2
        elif h%2 !=0:
            c[i]=h
            i+=2
    while c[len(c)-1]=='':
        del(c[len(c)-1])
    # print(array)
    # print(c)
# array =[22,24,26,28,30,1]
# qishu(array)

def userinfo_format():
    file1 = open('a1.txt')
    file2 = open('a2.txt','w+')
    while True:
        line = file1.readline()
        if len(line)==0:
            break
        # print(line)
        s = list(line)
        # print(s)
        index=0
        while (u'\u4e00' <= s[index] <= u'\u9fff'):
            index+=1
        s.insert(index,', ')
        s1 = ''.join(s)
        # print(s1)
        file2.write(s1)
    file1.close()
    file2.close()

# userinfo_format()

def countwords():
    file11 = open('aa.txt')
    dict1={}
    while True:
        line =  file11.readline()
        if(len(line)==0):
            break
        line1 = line.strip('\n')
        if (line1 in dict1 ):
            dict1[line1] +=1
        else:
            dict1[line1] = 1
    file11.close()
    # print(dict1)
    a = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
    # print(a)
    b=[]
    if len(a)>=5:
        for i in range(0,5):
           b.append(a[i][0])
    else:
        for j in a:
            b.append(j[0])
    return b
# print(countwords())
# file11.close()

def insertbigdata(n):
    number = 1
    file = open("bigdata.txt","w+")

    while(number <n):
        str2 = ran_strx('abcdefghijklmnopqrst我是方向001', 50)
        str1 = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤",2)
        list1 = [number,str1,random.randint(1,100),str2]
        print(list1)
        str3 = '|'.join('%s' % id for id in list1)
        str3 += '\r'
        file.write(str3)
        number+=1
    file.close()

def readdata(n):
    file1 = open("bigdata.txt")
    # num=0
    sumtime=0
    while (True):
        time1 = time.localtime()
        print(time.localtime())
        line = file1.readline()
        if len(line) == 0:
            break
        # print(line,type(line))
        list= line.split('|')
        sql ="insert into bigdata(id, name,luky,descript) values(%s,%s,%s,%s)"
        param = [int(list[0]),list[1],int(list[2]),list[3].strip('\n')]
        # print(param)
        # print(sql)
        helper = MysqlHelper()
        row = helper.insert(sql,param)
        # num +=1
        time2 = time.localtime()
        # timecha = time2-time1
        # sumtime + = timecha
    file1.close()
readdata(2)
    
























