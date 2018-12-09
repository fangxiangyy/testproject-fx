import unittest
import requests
import HTMLTestRunner


class Mytest(unittest.TestCase):
    def test_regist_1(self):
        url = 'http://localhost:8088/regist1'
        postData = {'username': 'tt1', 'password': 'tt1'}
        response = requests.post(url, data='username=tt1&password=tt1')
        content = response.json()
        # print(response.text)
        # print(content)
        r=self.assertEquals(content['rer']['msg'],'注册成功')
    def test_regist_2(self):

        # print(response.text)
        # print(content)
        content = registparm('t1','t1')
        r=self.assertEquals(content['rer']['msg'],'成功')
        print(content['rer']['msg'])


def registparm(username,password):
    url = 'http://localhost:8088/regist1'
    postData = {'username': username, 'password': password}
    response = requests.post(url, data=postData)
    content = response.json()
    return content

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(Mytest('test_regist_1'))
    test_suite.addTest(Mytest('test_regist_2'))
    fb = open('res.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fb,title='api测试报告',description='测试情况')
    runner.run(test_suite)
    fb.close()