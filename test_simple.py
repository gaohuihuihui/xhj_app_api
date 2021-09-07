import pytest


# 文件名  test_开头或者 _test结尾
# 类 Test开头
# 函数 test_开头
def inx(x):
    return x+1

def test_answer():
    assert inx(4)==5


class TestDemo():
    def test_demo1(self):
        pass
    def test_demo2(self):
        pass
