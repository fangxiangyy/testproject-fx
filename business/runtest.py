import unittest
from business.mytest  import Mytest
import HTMLTestRunner

test_suite = unittest.TestSuite()
test_suite.addTest(Mytest('test_regist_1'))
test_suite.addTest(Mytest('test_regist_2'))
fb = open('res.html', 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title='api测试报告', description='测试情况')
runner.run(test_suite)
fb.close()