import math
import unittest


def add(num1,num2):
    return num1+num2

def divide(num1,num2):
    if(isinstance(num1, int) or isinstance(num1, str)) \
            and (isinstance(num2, int) or isinstance(num2, str)):
        try:
            if (isinstance(num1, str)):
                num1 = int(num1)
            if(isinstance(num2,str)):
                num2 = int(num2)
        except(ValueError):
            return "请输入正确的参数，必须是整数或能转为整数的字符串"
        try:
            return math.trunc(num1/num2)
        except(ZeroDivisionError):
            return "除数不能为零"
    else:
        return "请输入正确的参数，必须是整数或能转为整数的字符串"

    # else:
    #     return num1/num2


class TestComputer(unittest.TestCase):
    def test_fushu(self):
        self.assertEqual(0,add(-1,1))
        # print(1)

    def test_bignum(self):
        self.assertEqual(10000000001,add(10000000000,1))
        # print(2)

    def test_bigfushu(self):
        self.assertEqual(-10000000001,add(-10000000000,-1))
        # print(3)

    def test_quzheng(self):
        self.assertEqual(5,divide(15,3))

    def test_ling(self):
        self.assertEqual('除数不能为零',divide(15,0))

    def test_str(self):
        self.assertEqual('请输入正确的参数，必须是整数或能转为整数的字符串',divide('aa','bb'))

    def test_str(self):
        self.assertEqual(5,divide('15','3'))

    def test_zhtrun(self):
        self.assertEqual(3,divide('15','4'))


if(__name__ == '__main__'):
    # testcomputer = TestComputer()
    # testcomputer.run()
    unittest.main
