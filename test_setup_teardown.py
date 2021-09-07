

# 模块级（setup_module/teardown_module)开始于横块始末，全局的
#
# 函数级（setup_function/teardown_function）只对函数用例生效（不在类中）
#
# 类级（setup_class/teardown_calss）只在类中前后运行一次（在类中）
#
# 方法级(setup_method/teardown_method)开始于方法始末(在类中)
#
# 类里面的（setup/teardown）运行在调用方法前后

def setup_module():
    print("setup module")

def teardown_module():

    print("teardown module")

def test_demo1():
    print("demo1")
    pass

def setup_function():
    print("setup function")

def teardown_function():
    print("teardown function")
