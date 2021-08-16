一：用例的识别与运行
    用例编写规范

        测试文件以test_开头(或者以_test结尾)

        pytest会找当前以及递归查找子文件夹下面所有的test_*.py或*_test.py的文件，把其当作测试文件（除非显式指定文件所在路径）

        测试类名称以Test开头，并且不能带有init方法

        如果类名称以Test开头的class类中包含了init方法，则会触发告警，提示PytestCollectionWarning: cannot collect test class 'TestXXX'

        测试函数以test_开头

        断言使用基本的assert即可

二：pytest装饰器
    pytest fixtures
        pytest中可以使用@pytest.fixture装饰器来装饰一个方法，
        被装饰方法的方法名可以作为一个参数传入到测试方法中。可以通过这种方式来完成测试之前的初始化操作，也可以返回数据给测试函数。
        import pytestclass
        TestFixture:
            @pytest.fixture()
            def login(self):
                return 11

            def test_001(self, login):
                assert 1+10 ==login

    fixture的scope参数:
        根据作用范围大小范围划分，分别是：session>module>class>function.
        @pytest.fixture(scope='function') scope的默认值是function
        function函数或者方法级别都会被调用

        class类级别调用一次

        module模块级别调用一次

        session是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module

    fixture的autouse参数
        如果想让每条测试用例都添加fixture功能，那么可以使用@pytest.fixture里面的autouse参数，autouse='true'则会自动应用到所有用例中。

    使用fixture传递测试数据
        fixture的param参数可以用来传递测试数据，实现数据驱动的效果，避免出现冗余代码。
        可以大大减少代码量，并且便于阅读和维护。传入的数据需要使用一个固定的参数名request来接收，代码如下：
        import pytest
        @pytest.fixture(params={1,2,3})
        def data(request):
          return request.param
        def test_data(data):
          print("测试数据{data}")
          assert data<10

三：conftest.py文件
    一般用于scope='session'级别的fixture。conftest.py被pytest视为一个本地插件库，使用conftest.py的规则：
        1、conftest.py这个文件名是固定的，不可以更改

        2、conftest.py与运行用例在同一个包下，并且该包中要有__init__.py文件

        3、使用的时候不需要导入conftest.py，pytest会自动加载，放到哪个package下，就在这个package内有效。

四：pytest断言
    assert关键字：

    assert xx：判断xx为真

    assert not xx：判断xx不为真

    assert a in b：判断b是否包含a

    assert a == b：判断a等于b

    assert a !=b：判断a不等于b

五：pytest parametrize参数化
   先来看一下parametrize()的方法源码
    def parametrize(self,argnames, argvalues, indirect=False, ids=None, scope=None):
    主要参数说明：

    argsnames:参数名，是一个字符串，多个参数名中间可以用逗号分隔

    argsvalues:参数对应的值，是由参数组成的列表，列表中有几个元素，就会生成几条用例，参数名和参数值的数量要相等。

    indirect:该参数值默认为False，表示argnames就是普通的参数，如果将该值设置为True，则可以用来将参数传入到fixture方法中。

    ids:用于标志用例的一个id字段，默认可以不传，会自动用argvalues填充，ids参数可以用来区分测试方法的标识。

    scope:声明argnames中参数的作用域，进而影响到测试用例的收集顺序

