import pytest
import allure
from apilist.meizikuApi import send_requests
from common.readYaml import ReadFileData
from common.db_execMySQL import con
from conf.meiziku import sql_appkey
import logging
from common.logger import Logging

Logging()


#实例化读取配置文件的类,获取配置文件
readFileData=ReadFileData()
data=readFileData.get_data('test_data/ParamYaml','meiziku_api.yml')

#   //以下是定义的初始化、清除方法//
@pytest.fixture(scope="function",autouse=False)
def createAccesskey(login_start):
    '''删除接口的初始化动作：新建accesskey'''
    logging.info("初始化操作:创建accesskey")
    token = login_start
    method = data["create_appkey"][0]["Method"]
    apiurl = data["create_appkey"][0]["ApiUrl"]
    params = data["create_appkey"][1]["Params"]
    response = send_requests(method, apiurl, token, data=params)
    return response['value']['id']

def delete_accesskey(token,id):
        '''删除appkey,用作新建测试用例的清除操作'''
        method = data["delete_appkey"][0]["Method"]
        apiurl = data["delete_appkey"][0]["ApiUrl"]
        params = {"id":id}
        response = send_requests(method, apiurl, token, params=params)

#   //以下是测试用例//
@allure.feature("媒资库后台管理")
@allure.story("管理后台access接口")
@allure.title("获取appkey-传入参数q,参数值正确")
@allure.description("传入参数q,参数值正确")
def test_getAccesskey_001(login_start):
        token =login_start
        method=data["get_appkey"][0]["Method"]
        apiurl=data["get_appkey"][0]["ApiUrl"]
        params=data["get_appkey"][0]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        #断言
        assert response['code']=='0'
        assert response['value'][0]['name']==params['q']

@allure.feature("媒资库后台管理")
@allure.story("管理后台access接口")
@allure.title("获取appkey-传入参数q,参数值不正确")
@allure.description("传入参数q,参数值不正确")
def test_getAccesskey_002(login_start):
        token =login_start
        method=data["get_appkey"][1]["Method"]
        apiurl=data["get_appkey"][1]["ApiUrl"]
        params=data["get_appkey"][1]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        #断言
        assert response['code']=='0'
        assert response['value']==[]

@allure.feature("媒资库后台管理")
@allure.story("管理后台access接口")
@allure.title("获取appkey-传入参数q,参数值为空")
@allure.description("传入参数q,参数值为空")
def test_getAccesskey_003(login_start):
        token =login_start
        method=data["get_appkey"][2]["Method"]
        apiurl=data["get_appkey"][2]["ApiUrl"]
        params=data["get_appkey"][2]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        #断言
        exe_rlt = con.get_data(sql_appkey)  # 期望输出
        print(exe_rlt)
        assert response['code'] == '0'
        assert len(response['value']) == len(exe_rlt)

@allure.feature("媒资库后台管理")
@allure.story("管理后台access接口")
@allure.title("获取appkey-不传参数")
@allure.description("不传参数")
def test_getAccesskey_004(login_start):
        token =login_start
        method=data["get_appkey"][3]["Method"]
        apiurl=data["get_appkey"][3]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        #断言
        exe_rlt = con.get_data(sql_appkey)  # 期望输出
        print(exe_rlt)
        assert response['code'] == '0'
        assert len(response['value']) == len(exe_rlt)


@allure.feature("媒资库后台管理")
@allure.story("管理后台access接口")
@allure.title("创建appkey-传入参数q,参数值在数据库中不存在")
@allure.description("传入参数q,参数值正确")
def test_createAccesskey_001(login_start):
        token =login_start
        method=data["create_appkey"][0]["Method"]
        apiurl=data["create_appkey"][0]["ApiUrl"]
        params=data["create_appkey"][0]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        id=response['value']['id']
        # 断言
        assert response['code'] == '0'
        assert response['value']['name'] == params['name']

        #执行清除操作，删除创建的appkey
        delete_accesskey(token,id)

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台access接口")
@allure.title("创建appkey-传入参数q,参数值在数据库中已存在")
@allure.description("传入参数q,参数值不正确")
def test_createAccesskey_002(login_start):
        token =login_start
        method=data["create_appkey"][0]["Method"]
        apiurl=data["create_appkey"][0]["ApiUrl"]
        params=data["create_appkey"][2]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        # 断言
        assert response['code'] == '0'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台access接口")
@allure.title("创建appkey-传入参数q,参数值为空")
@allure.description("传入参数q,参数值为空")
def test_createAccesskey_003(login_start):
        token =login_start
        method=data["create_appkey"][0]["Method"]
        apiurl=data["create_appkey"][0]["ApiUrl"]
        params=data["create_appkey"][3]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        # 断言
        assert response['code'] == '0'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台access接口")
@allure.title("创建appkey-不传参数")
@allure.description("不传参数")
def test_createAccesskey_004(login_start):
        token =login_start
        method=data["create_appkey"][0]["Method"]
        apiurl=data["create_appkey"][0]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        # 断言
        assert response['code'] == '0'

@allure.feature("媒资库后台管理")
@allure.story("管理后台access接口")
@allure.title("删除appkey-传入参数id,参数值正确")
@allure.description("传入参数id,参数值正确")
def test_deleteAccesskey_001(createAccesskey,login_start):
        '''
        :param createAccesskey: 初始化动作的方法名
        :param login_start: 登录接口，用户获取token
        :return:
        '''
        token =login_start
        print(createAccesskey)
        method=data["delete_appkey"][0]["Method"]
        apiurl=data["delete_appkey"][0]["ApiUrl"]
        params=data["delete_appkey"][0]["Params"]
        #将params中的id值更新成创建accesskey后对于的id
        params['id']=createAccesskey
        response=send_requests(method,apiurl,token,params=params)
        # 断言
        assert response['code'] == '0'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台access接口")
@allure.title("删除appkey-传入参数id,参数值不正确")
@allure.description("传入参数id,参数值不正确")
def test_deleteAccesskey_002(login_start):
        '''
        :param createAccesskey: 初始化动作的方法名
        :param login_start: 登录接口，用户获取token
        :return:
        '''
        token =login_start
        method=data["delete_appkey"][1]["Method"]
        apiurl=data["delete_appkey"][1]["ApiUrl"]
        params=data["delete_appkey"][1]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        # 断言
        assert response['value'] != True

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台access接口")
@allure.title("删除appkey-传入参数id,参数值为空")
@allure.description("传入参数id,参数值为空")
def test_deleteAccesskey_003(login_start):
        '''
        :param createAccesskey: 初始化动作的方法名
        :param login_start: 登录接口，用户获取token
        :return:
        '''
        token =login_start
        method=data["delete_appkey"][2]["Method"]
        apiurl=data["delete_appkey"][2]["ApiUrl"]
        params=data["delete_appkey"][2]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        # 断言
        assert response['value'] != True

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台access接口")
@allure.title("删除appkey-不传参数")
@allure.description("不传参数")
def test_deleteAccesskey_004(login_start):
        '''
        :param createAccesskey: 初始化动作的方法名
        :param login_start: 登录接口，用户获取token
        :return:
        '''
        token =login_start
        method=data["delete_appkey"][2]["Method"]
        apiurl=data["delete_appkey"][2]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        # 断言
        assert response['value'] !=True



if __name__ == "__main__":
    # pytest.main(["-s","test_accesskey.py"])
    pytest.main(["-s","test_accesskey.py"])

