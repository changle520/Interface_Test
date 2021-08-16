import pytest
import allure
from apilist.login import login
from common.hashlibSHA1 import get_str_sha1
from common.readYaml import ReadFileData

#实例化读取配置文件的类,获取配置文件
readFileData=ReadFileData()
data=readFileData.get_data('test_data/ParamYaml','meiziku_api.yml')

@allure.feature("媒资库后台管理")
@allure.story("管理后台User接口")
@allure.title("登录接口--正确的用户名、密码")
@allure.description("传入正确的用户名、密码")
def test_login001():
    username=data['login'][0]['Params']['username']
    password=data['login'][0]['Params']['password']
    # 对密码进行加密
    password = get_str_sha1(password)
    response=login(username=username,password=password)
    # 断言
    assert response['response']['code'] == '0'
    assert response['response']['value']['username'] == username

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台User接口")
@allure.title("登录接口--错误的用户名、密码")
@allure.description("传入错误的用户名、密码")
def test_login002():
    username=data['login'][1]['Params']['username']
    password=data['login'][1]['Params']['password']
    # 对密码进行加密
    password = get_str_sha1(password)
    response=login(username=username,password=password)
    # 断言
    assert response['response']['code'] == '0'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台User接口")
@allure.title("登录接口--正确的用户名、错误的密码")
@allure.description("传入正确的用户名、错误的密码")
def test_login003():
    username=data['login'][2]['Params']['username']
    password=data['login'][2]['Params']['password']
    # 对密码进行加密
    password = get_str_sha1(password)
    response=login(username=username,password=password)
    # 断言
    assert response['response']['code'] == '0'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台User接口")
@allure.title("登录接口--错误的用户名、正确的密码")
@allure.description("传入错误的用户名、正确的密码")
def test_login004():
    username=data['login'][3]['Params']['username']
    password=data['login'][3]['Params']['password']
    # 对密码进行加密
    password = get_str_sha1(password)
    response=login(username=username,password=password)
    # 断言
    assert response['response']['code'] == '0'
    assert response['response']['message'] == '服务端业务处理异常'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台User接口")
@allure.title("登录接口--用户名、密码为空")
@allure.description("用户名、密码为空")
def test_login005():
    username=data['login'][4]['Params']['username']
    password=data['login'][4]['Params']['password']
    # 对密码进行加密
    password = get_str_sha1(password)
    response=login(username=username,password=password)
    # 断言
    assert response['response']['code'] == '0'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台User接口")
@allure.title("登录接口--不传密码")
@allure.description("不传密码")
def test_login006():
    username=data['login'][5]['Params']['username']
    print(username)
    response=login(username=username)
    # 断言
    assert response['response']['code'] == '0'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台User接口")
@allure.title("登录接口--不传用户名")
@allure.description("不传用户名")
def test_login006():
    password=data['login'][6]['Params']['password']
    password = get_str_sha1(password)
    response=login(password=password)
    # 断言
    assert response['response']['code'] == '0'

if __name__ == '__main__':
    pytest.main(['-s',"test_login.py::test_login006"])