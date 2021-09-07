import pytest
#单参数
list=["Tom","jjj"]

@pytest.mark.parametrize('name',list)
def test_search(name):
    pass
    print("dddd"+name)