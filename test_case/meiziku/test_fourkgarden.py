import pytest
import allure
from apilist.meizikuApi import send_requests
from common.readYaml import ReadFileData
from common.db_execMySQL import con
from conf.meiziku import sql_sync_log

#实例化读取配置文件的类,获取配置文件
readFileData=ReadFileData()
data=readFileData.get_data('test_data/ParamYaml','meiziku_api.yml')

@allure.feature("媒资库后台管理")
@allure.story("管理后台4k花园接口")
@allure.title("4k花园同步影片")
@allure.description("不传入参数")
def test_skgarden_sync(login_start):
        token =login_start
        method=data["skgarden_sync"][0]["Method"]
        apiurl=data["skgarden_sync"][0]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        #断言
        assert response['code'] == '0'
        assert response['value']== True

@allure.feature("媒资库后台管理")
@allure.story("管理后台4k花园接口")
@allure.title("4k花园当前同步状态")
@allure.description("不传入参数")
def test_skgarden_syncs_status(login_start):
        token =login_start
        method=data["skgarden_sync_status"][0]["Method"]
        apiurl=data["skgarden_sync_status"][0]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        # 断言
        assert response['code'] == '0'
        assert response['value'] == 'syncing'

@allure.feature("媒资库后台管理")
@allure.story("管理后台4k花园接口")
@allure.title("4k花园同步记录-传入参数page,size、参数值正确")
@allure.description("传入参数page,size")
def test_skgarden_synclog001(login_start):
        token =login_start
        method=data["skgarden_synclog"][0]["Method"]
        apiurl=data["skgarden_synclog"][0]["ApiUrl"]
        params = data["skgarden_synclog"][0]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        # 断言
        exe_rlt = con.get_data(sql_sync_log)  # 期望输出
        assert response['value']['total'] == len(exe_rlt)
        assert response['code'] == '0'
        assert response['value']['current'] == 1

@allure.feature("媒资库后台管理")
@allure.story("管理后台4k花园接口")
@allure.title("4k花园同步记录-不传参数")
@allure.description("不传参数")
def test_skgarden_synclog002(login_start):
        token =login_start
        method=data["skgarden_synclog"][1]["Method"]
        apiurl=data["skgarden_synclog"][1]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        # 断言
        assert response['code'] == '0'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台4k花园接口")
@allure.title("4k花园同步记录-传入参数page,size、page的内容为1,size的内容为空")
@allure.description("传入参数page,size")
def test_skgarden_synclog003(login_start):
        token =login_start
        method=data["skgarden_synclog"][2]["Method"]
        apiurl=data["skgarden_synclog"][2]["ApiUrl"]
        params = data["skgarden_synclog"][2]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        # 断言
        assert response['code'] == '0'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台4k花园接口")
@allure.title("4k花园同步记录-传入参数page,size、page的内容为空,size的内容为20")
@allure.description("传入参数page,size")
def test_skgarden_synclog004(login_start):
        token =login_start
        method=data["skgarden_synclog"][3]["Method"]
        apiurl=data["skgarden_synclog"][3]["ApiUrl"]
        params = data["skgarden_synclog"][3]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        # 断言
        assert response['code'] == '0'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台4k花园接口")
@allure.title("4k花园同步记录-传入参数page,size、内容都为空")
@allure.description("传入参数page,size")
def test_skgarden_synclog005(login_start):
        token =login_start
        method=data["skgarden_synclog"][4]["Method"]
        apiurl=data["skgarden_synclog"][4]["ApiUrl"]
        params = data["skgarden_synclog"][4]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        # 断言
        assert response['code'] == '0'


@allure.feature("媒资库后台管理")
@allure.story("管理后台4k花园接口")
@allure.title("获取4K花园影片列表-分页-传入参数page,size,q 参数值正确")
@allure.description("传入参数page,size,q 参数值正确")
def test_skgarden_skgardenvideo_list_001(login_start):
        token =login_start
        method=data["skgardenvideo_list"][0]["Method"]
        apiurl=data["skgardenvideo_list"][0]["ApiUrl"]
        params = data["skgardenvideo_list"][0]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        # 断言
        assert response['code'] == '0'
        assert response['value']['current'] == 1
        assert response['value']['data'][0]['name']==params["q"]

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台4k花园接口")
@allure.title("获取4K花园影片列表-分页-不传参数")
@allure.description("不传参数")
def test_skgarden_skgardenvideo_list_002(login_start):
        token =login_start
        method=data["skgardenvideo_list"][1]["Method"]
        apiurl=data["skgardenvideo_list"][1]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        # 断言
        assert response['code'] == '0'

@allure.feature("媒资库后台管理")
@allure.story("管理后台4k花园接口")
@allure.title("获取4K花园影片列表-分页-传入参数page,size,q q的值为空")
@allure.description("传入参数page,size,q q的值为空")
def test_skgarden_skgardenvideo_list_003(login_start):
        token =login_start
        method=data["skgardenvideo_list"][2]["Method"]
        apiurl=data["skgardenvideo_list"][2]["ApiUrl"]
        params = data["skgardenvideo_list"][2]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        # 断言
        assert response['code'] == '0'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台4k花园接口")
@allure.title("获取4K花园影片列表-分页-传入page,不传size")
@allure.description("传入page,不传size")
def test_skgarden_skgardenvideo_list_004(login_start):
        token =login_start
        method=data["skgardenvideo_list"][3]["Method"]
        apiurl=data["skgardenvideo_list"][3]["ApiUrl"]
        params = data["skgardenvideo_list"][3]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        # 断言
        assert response['code'] == '0'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台4k花园接口")
@allure.title("获取4K花园影片列表-分页-传入size,不传page")
@allure.description("传入size,不传page")
def test_skgarden_skgardenvideo_list_005(login_start):
        token =login_start
        method=data["skgardenvideo_list"][4]["Method"]
        apiurl=data["skgardenvideo_list"][4]["ApiUrl"]
        params = data["skgardenvideo_list"][4]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        # 断言
        assert response['code'] == '0'


if __name__ == '__main__':
    # pytest.main(['-s',"test_fourkgarden.py"])
    pytest.main(['-s',"test_fourkgarden.py"])