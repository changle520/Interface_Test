import pytest
import allure
from apilist.meizikuApi import send_requests
from common.readYaml import ReadFileData
from conf.meiziku import sql_config,sql_template
from common.db_execMySQL import con

#实例化读取配置文件的类,获取配置文件
readFileData=ReadFileData()
data=readFileData.get_data('test_data/ParamYaml','meiziku_api.yml')

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("获取配置项")
@allure.description("不传入参数")
def test_core_config(login_start):
        token =login_start
        method=data["core_config"][0]["Method"]
        apiurl=data["core_config"][0]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        # 断言
        exe_rlt=con.get_data(sql_config) #期望输出
        print(exe_rlt)
        assert response['code'] == '0'
        assert len(response['value']) == len(exe_rlt)

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("获取job列表-分页")
@allure.description("传入参数page,size,q 参数值正确")
def test_job_list001(login_start):
        token =login_start
        method=data["job_list"][0]["Method"]
        apiurl=data["job_list"][0]["ApiUrl"]
        params = data["job_list"][0]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        assert response['code'] == '0'
        assert response['value']['current'] == 1
        assert len(response['value']['data']) > 0   #通过什么字段搜索还在确认中、待确认后同步这里的断言内容

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-修改演员")
@allure.description("传入参数id,actors,参数值正确")
def test_modify_originalvideo001(login_start):
        token =login_start
        method=data["modify_originalvideo"][0]["Method"]
        apiurl=data["modify_originalvideo"][0]["ApiUrl"]
        params = data["modify_originalvideo"][0]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-不传参数")
@allure.description("不传参数")
def test_modify_originalvideo002(login_start):
        token =login_start
        method=data["modify_originalvideo"][1]["Method"]
        apiurl=data["modify_originalvideo"][1]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        assert response['code'] == '0'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-传入参数id,参数值为空")
@allure.description("传入参数id,参数值为空")
def test_modify_originalvideo003(login_start):
        token =login_start
        method=data["modify_originalvideo"][2]["Method"]
        apiurl=data["modify_originalvideo"][2]["ApiUrl"]
        params = data["modify_originalvideo"][2]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-修改背景图")
@allure.description("传入参数id,background,参数值正确")
def test_modify_originalvideo004(login_start):
        token =login_start
        method=data["modify_originalvideo"][3]["Method"]
        apiurl=data["modify_originalvideo"][3]["ApiUrl"]
        params = data["modify_originalvideo"][3]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-修改描述")
@allure.description("传入参数id,description,参数值正确")
def test_modify_originalvideo005(login_start):
        token =login_start
        method=data["modify_originalvideo"][4]["Method"]
        apiurl=data["modify_originalvideo"][4]["ApiUrl"]
        params = data["modify_originalvideo"][4]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-id不存在")
@allure.description("传入参数id,id不存在")
def test_modify_originalvideo006(login_start):
        token =login_start
        method=data["modify_originalvideo"][5]["Method"]
        apiurl=data["modify_originalvideo"][5]["ApiUrl"]
        params = data["modify_originalvideo"][5]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-修改导演")
@allure.description("传入参数id,director,参数值正确")
def test_modify_originalvideo007(login_start):
        token =login_start
        method=data["modify_originalvideo"][6]["Method"]
        apiurl=data["modify_originalvideo"][6]["ApiUrl"]
        params = data["modify_originalvideo"][6]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-修改配音(id)")
@allure.description("传入参数id,dubbingId,参数值正确")
def test_modify_originalvideo008(login_start):
        token =login_start
        method=data["modify_originalvideo"][7]["Method"]
        apiurl=data["modify_originalvideo"][7]["ApiUrl"]
        params = data["modify_originalvideo"][7]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-修改竖版海报")
@allure.description("传入参数id,horizontal,参数值正确")
def test_modify_originalvideo009(login_start):
        token =login_start
        method=data["modify_originalvideo"][8]["Method"]
        apiurl=data["modify_originalvideo"][8]["ApiUrl"]
        params = data["modify_originalvideo"][8]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-播放格式为1")
@allure.description("传入参数id,playerFormatKey,playerFormatKey=1")
def test_modify_originalvideo010(login_start):
        token =login_start
        method=data["modify_originalvideo"][9]["Method"]
        apiurl=data["modify_originalvideo"][9]["ApiUrl"]
        params = data["modify_originalvideo"][9]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-播放格式为2")
@allure.description("传入参数id,playerFormatKey,playerFormatKey=2")
def test_modify_originalvideo011(login_start):
        token =login_start
        method=data["modify_originalvideo"][10]["Method"]
        apiurl=data["modify_originalvideo"][10]["ApiUrl"]
        params = data["modify_originalvideo"][10]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-播放格式为3")
@allure.description("传入参数id,playerFormatKey,playerFormatKey=3")
def test_modify_originalvideo012(login_start):
        token =login_start
        method=data["modify_originalvideo"][11]["Method"]
        apiurl=data["modify_originalvideo"][11]["ApiUrl"]
        params = data["modify_originalvideo"][11]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-播放格式传参为字符串")
@allure.description("传入参数id,playerFormatKey,playerFormatKey为字符串")
def test_modify_originalvideo013(login_start):
        token =login_start
        method=data["modify_originalvideo"][12]["Method"]
        apiurl=data["modify_originalvideo"][12]["ApiUrl"]
        params = data["modify_originalvideo"][12]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] != True

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-编辑地区")
@allure.description("传入参数id,regionId")
def test_modify_originalvideo014(login_start):
        token =login_start
        method=data["modify_originalvideo"][13]["Method"]
        apiurl=data["modify_originalvideo"][13]["ApiUrl"]
        params = data["modify_originalvideo"][13]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-编辑评分")
@allure.description("传入参数id,score")
def test_modify_originalvideo015(login_start):
        token =login_start
        method=data["modify_originalvideo"][14]["Method"]
        apiurl=data["modify_originalvideo"][14]["ApiUrl"]
        params = data["modify_originalvideo"][14]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-编辑短描述")
@allure.description("传入参数id,shortDescription")
def test_modify_originalvideo016(login_start):
        token =login_start
        method=data["modify_originalvideo"][15]["Method"]
        apiurl=data["modify_originalvideo"][15]["ApiUrl"]
        params = data["modify_originalvideo"][15]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-编辑横板海报")
@allure.description("传入参数id,vertical")
def test_modify_originalvideo017(login_start):
        token =login_start
        method=data["modify_originalvideo"][16]["Method"]
        apiurl=data["modify_originalvideo"][16]["ApiUrl"]
        params = data["modify_originalvideo"][16]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-编辑视频类型为2D")
@allure.description("传入参数id,videoFormatKey")
def test_modify_originalvideo018(login_start):
        token =login_start
        method=data["modify_originalvideo"][17]["Method"]
        apiurl=data["modify_originalvideo"][17]["ApiUrl"]
        params = data["modify_originalvideo"][17]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-编辑视频类型为3D左右")
@allure.description("传入参数id,videoFormatKey")
def test_modify_originalvideo019(login_start):
        token =login_start
        method=data["modify_originalvideo"][18]["Method"]
        apiurl=data["modify_originalvideo"][18]["ApiUrl"]
        params = data["modify_originalvideo"][18]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-编辑视频类型为3D上下")
@allure.description("传入参数id,videoFormatKey")
def test_modify_originalvideo020(login_start):
        token =login_start
        method=data["modify_originalvideo"][19]["Method"]
        apiurl=data["modify_originalvideo"][19]["ApiUrl"]
        params = data["modify_originalvideo"][19]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-编辑视频类型为不存在的内容")
@allure.description("传入参数id,videoFormatKey")
def test_modify_originalvideo021(login_start):
        token =login_start
        method=data["modify_originalvideo"][20]["Method"]
        apiurl=data["modify_originalvideo"][20]["ApiUrl"]
        params = data["modify_originalvideo"][20]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] != True

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-编辑片名")
@allure.description("传入参数id,videoname")
def test_modify_originalvideo022(login_start):
        token =login_start
        method=data["modify_originalvideo"][21]["Method"]
        apiurl=data["modify_originalvideo"][21]["ApiUrl"]
        params = data["modify_originalvideo"][21]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("编辑影片详情-编辑年代")
@allure.description("传入参数id,years")
def test_modify_originalvideo023(login_start):
        token =login_start
        method=data["modify_originalvideo"][22]["Method"]
        apiurl=data["modify_originalvideo"][22]["ApiUrl"]
        params = data["modify_originalvideo"][22]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("获取影片详情")
@allure.description("传入参数id 参数值正确")
def test_get_originalvideo001(login_start):
        token =login_start
        method=data["get_originalvideo"][0]["Method"]
        apiurl=data["get_originalvideo"][0]["ApiUrl"]
        params = data["get_originalvideo"][0]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        #断言
        assert response['code'] == '0'
        assert response['value']['id'] == str(params['id'])

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("获取影片详情-不传任何参数")
@allure.description("不传任何参数")
def test_get_originalvideo002(login_start):
        token =login_start
        method=data["get_originalvideo"][1]["Method"]
        apiurl=data["get_originalvideo"][1]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        #断言
        assert response['code'] == '0'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("获取影片详情-参数值不正确")
@allure.description("传入参数id 参数值不正确")
def test_get_originalvideo003(login_start):
        token =login_start
        method=data["get_originalvideo"][2]["Method"]
        apiurl=data["get_originalvideo"][2]["ApiUrl"]
        params = data["get_originalvideo"][2]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        #断言
        assert response['code'] == '0'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("获取影片详情- 参数值为空")
@allure.description("传入参数id 参数值为空")
def test_get_originalvideo004(login_start):
        token =login_start
        method=data["get_originalvideo"][3]["Method"]
        apiurl=data["get_originalvideo"][3]["ApiUrl"]
        params = data["get_originalvideo"][3]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        #断言
        assert response['code'] == '0'

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("获取自有原片列表-分页")
@allure.description("传入参数page,size,q 参数值正确")
def test_originalvideo_list001(login_start):
        token =login_start
        method=data["originalvideo_list"][0]["Method"]
        apiurl=data["originalvideo_list"][0]["ApiUrl"]
        params = data["originalvideo_list"][0]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        # 断言
        assert response['code'] == '0'
        assert response['value']['data'][0]['videoName'] == params['q']

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("获取自有原片列表-分页-传入参数page,size,q q的值为空")
@allure.description("传入参数page,size,q q的值为空")
def test_originalvideo_list002(login_start):
        token =login_start
        method=data["originalvideo_list"][1]["Method"]
        apiurl=data["originalvideo_list"][1]["ApiUrl"]
        params = data["originalvideo_list"][1]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        # 断言
        assert response['code'] == '0'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("获取自有原片列表-分页-传入参数page")
@allure.description("传入参数page")
def test_originalvideo_list003(login_start):
        token =login_start
        method=data["originalvideo_list"][2]["Method"]
        apiurl=data["originalvideo_list"][2]["ApiUrl"]
        params = data["originalvideo_list"][2]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        # 断言
        assert response['code'] == '1'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("获取自有原片列表-分页-传入参数size")
@allure.description("传入参数size")
def test_originalvideo_list004(login_start):
        token =login_start
        method=data["originalvideo_list"][3]["Method"]
        apiurl=data["originalvideo_list"][3]["ApiUrl"]
        params = data["originalvideo_list"][3]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        # 断言
        assert response['code'] == '1'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("获取自有原片列表-分页-不传参数")
@allure.description("不传参数")
def test_originalvideo_list005(login_start):
        token =login_start
        method=data["originalvideo_list"][3]["Method"]
        apiurl=data["originalvideo_list"][3]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        # 断言
        assert response['code'] == '1'

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("执行阿里云MPS转码切片")
@allure.description("传入参数encryption、id、templateId，参数的值正确")
def test_originalvideo_mps_transcode001(login_start):
        token =login_start
        method=data["originalvideo_mps_transcode"][0]["Method"]
        apiurl=data["originalvideo_mps_transcode"][0]["ApiUrl"]
        params = data["originalvideo_mps_transcode"][0]["Params"]
        headers=data["originalvideo_mps_transcode"][0]["headers"]
        response=send_requests(method,apiurl,token,headers,data=params)
        # 断言
        assert response['code'] == '0'
        assert response['value'] == True

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("执行阿里云MPS转码切片-不传参数")
@allure.description("不传参数")
def test_originalvideo_mps_transcode002(login_start):
        token =login_start
        method=data["originalvideo_mps_transcode"][1]["Method"]
        apiurl=data["originalvideo_mps_transcode"][1]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        # 断言
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("执行阿里云MPS转码切片-传入参数encryption，参数的值正确")
@allure.description("传入参数encryption，参数的值正确")
def test_originalvideo_mps_transcode003(login_start):
        token =login_start
        method=data["originalvideo_mps_transcode"][2]["Method"]
        apiurl=data["originalvideo_mps_transcode"][2]["ApiUrl"]
        params = data["originalvideo_mps_transcode"][2]["Params"]
        headers=data["originalvideo_mps_transcode"][2]["headers"]
        response=send_requests(method,apiurl,token,headers,data=params)
        # 断言
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("执行阿里云MPS转码切片-传入参数templateId，参数的值正确")
@allure.description("传入参数templateId，参数的值正确")
def test_originalvideo_mps_transcode004(login_start):
        token =login_start
        method=data["originalvideo_mps_transcode"][3]["Method"]
        apiurl=data["originalvideo_mps_transcode"][3]["ApiUrl"]
        params = data["originalvideo_mps_transcode"][3]["Params"]
        headers=data["originalvideo_mps_transcode"][3]["headers"]
        response=send_requests(method,apiurl,token,headers,data=params)
        # 断言
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("执行阿里云MPS转码切片-传入参数id，参数的值正确")
@allure.description("传入参数id，参数的值正确")
def test_originalvideo_mps_transcode005(login_start):
        token =login_start
        method=data["originalvideo_mps_transcode"][4]["Method"]
        apiurl=data["originalvideo_mps_transcode"][4]["ApiUrl"]
        params = data["originalvideo_mps_transcode"][4]["Params"]
        headers=data["originalvideo_mps_transcode"][4]["headers"]
        response=send_requests(method,apiurl,token,headers,data=params)
        # 断言
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("执行阿里云MPS转码切片-传入参数encryption、id、templateId、seek、duration，参数的值正确")
@allure.description("传入参数encryption、id、templateId、seek、duration，参数的值正确")
def test_originalvideo_mps_transcode006(login_start):
        token =login_start
        method=data["originalvideo_mps_transcode"][5]["Method"]
        apiurl=data["originalvideo_mps_transcode"][5]["ApiUrl"]
        params = data["originalvideo_mps_transcode"][5]["Params"]
        headers=data["originalvideo_mps_transcode"][5]["headers"]
        response=send_requests(method,apiurl,token,headers,data=params)
        # 断言
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("执行阿里云MPS转码切片-传入参数encryption、id、templateId、seek，参数的值正确")
@allure.description("-传入参数encryption、id、templateId、seek，参数的值正确")
def test_originalvideo_mps_transcode007(login_start):
        token =login_start
        method=data["originalvideo_mps_transcode"][6]["Method"]
        apiurl=data["originalvideo_mps_transcode"][6]["ApiUrl"]
        params = data["originalvideo_mps_transcode"][6]["Params"]
        headers=data["originalvideo_mps_transcode"][6]["headers"]
        response=send_requests(method,apiurl,token,headers,data=params)
        # 断言
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("执行阿里云MPS转码切片-传入参数encryption、id、templateId、duration，参数的值正确")
@allure.description("传入参数encryption、id、templateId、duration，参数的值正确")
def test_originalvideo_mps_transcode008(login_start):
        token =login_start
        method=data["originalvideo_mps_transcode"][7]["Method"]
        apiurl=data["originalvideo_mps_transcode"][7]["ApiUrl"]
        params = data["originalvideo_mps_transcode"][7]["Params"]
        headers=data["originalvideo_mps_transcode"][7]["headers"]
        response=send_requests(method,apiurl,token,headers,data=params)
        # 断言
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("执行阿里云MPS截图-参数值正确")
@allure.description("传入参数id 参数值正确")
def test_originalvideo_mps_snapshot001(login_start):
        token =login_start
        method=data["originalvideo_mps_snapshot"][0]["Method"]
        apiurl=data["originalvideo_mps_snapshot"][0]["ApiUrl"]
        params = data["originalvideo_mps_snapshot"][0]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        # 断言
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("执行阿里云MPS截图-参数值不正确")
@allure.description("传入参数id 参数值不正确")
def test_originalvideo_mps_snapshot002(login_start):
        token =login_start
        method=data["originalvideo_mps_snapshot"][1]["Method"]
        apiurl=data["originalvideo_mps_snapshot"][1]["ApiUrl"]
        params = data["originalvideo_mps_snapshot"][1]["Params"]
        response=send_requests(method,apiurl,token,params=params)
        # 断言
        assert response['code'] == '2005'
        assert response['message'] == '影片不存在'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("执行阿里云MPS截图-不传参数")
@allure.description("不传参数")
def test_originalvideo_mps_snapshot003(login_start):
        token =login_start
        method=data["originalvideo_mps_snapshot"][2]["Method"]
        apiurl=data["originalvideo_mps_snapshot"][2]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        # 断言
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("同步阿里云job状态")
@allure.description("不传参数")
def test_originalvideo_mps_sync_job(login_start):
        token =login_start
        method=data["originalvideo_mps_sync_job"][0]["Method"]
        apiurl=data["originalvideo_mps_sync_job"][0]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        # 断言
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("从阿里云同步切片模板")
@allure.description("不传参数")
def test_originalvideo_sync_template(login_start):
        token =login_start
        method=data["originalvideo_sync_template"][0]["Method"]
        apiurl=data["originalvideo_sync_template"][0]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        # 断言
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("从阿里云同步原片")
@allure.description("不传参数")
def test_originalvideo_sync_video(login_start):
        token =login_start
        method=data["originalvideo_sync_video"][0]["Method"]
        apiurl=data["originalvideo_sync_video"][0]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        # 断言
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("获取转码模板列表")
@allure.description("不传参数")
def test_transcodetemplatelist(login_start):
        token =login_start
        method=data["originalvideo_transcodetemplatelist"][0]["Method"]
        apiurl=data["originalvideo_transcodetemplatelist"][0]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        # 断言
        assert response['code'] == '0'
        exe_rlt = con.get_data(sql_template)  # 期望输出
        assert len(response['value']) == len(exe_rlt)

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("通过影片id删除影片-传入正确的影片id")
@allure.description("传入正确的影片id")
def test_originalvideo_delete001(login_start):
        token =login_start
        method=data["originalvideo_delete"][0]["Method"]
        apiurl=data["originalvideo_delete"][0]["ApiUrl"]
        params = data["originalvideo_delete"][0]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        # 断言
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("通过影片id删除影片-传入不存在的影片id")
@allure.description("传入不存在的影片id")
def test_originalvideo_delete002(login_start):
        token =login_start
        method=data["originalvideo_delete"][1]["Method"]
        apiurl=data["originalvideo_delete"][1]["ApiUrl"]
        params = data["originalvideo_delete"][1]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        # 断言
        assert response['code'] == '2005'
        assert response['message'] == '影片不存在'

@pytest.mark.xfail
@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("通过影片id删除影片-id是字符串")
@allure.description("传入id是字符串")
def test_originalvideo_delete003(login_start):
        token =login_start
        method=data["originalvideo_delete"][2]["Method"]
        apiurl=data["originalvideo_delete"][2]["ApiUrl"]
        params = data["originalvideo_delete"][2]["Params"]
        response=send_requests(method,apiurl,token,data=params)
        # 断言
        assert response['code'] == '0'

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("通过影片id删除影片切片-传入存在的影片id")
@allure.description("传入存在的影片id")
def test_originalvideo_delete_alldefination001(login_start):
        token =login_start
        method=data["originalvideo_delete_alldefination"][0]["Method"]
        apiurl=data["originalvideo_delete_alldefination"][0]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        # 断言
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("通过影片id删除影片切片-传入不存在的影片id")
@allure.description("传入不存在的影片id,id中有字符串")
def test_originalvideo_delete_alldefination002(login_start):
        token =login_start
        method=data["originalvideo_delete_alldefination"][1]["Method"]
        apiurl=data["originalvideo_delete_alldefination"][1]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        # 断言
        assert response['code'] == '2005'
        assert response['message'] == '影片不存在'

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("获取影片标准主M3U8-传入存在的影片id")
@allure.description("传入存在的影片id")
def test_originalvideo_standard_m3u8_001(login_start):
        token =login_start
        method=data["originalvideo_delete_alldefination"][0]["Method"]
        apiurl=data["originalvideo_delete_alldefination"][0]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        # 断言
        assert response['code'] == '0'
        assert response['value'] == True

@allure.feature("媒资库后台管理")
@allure.story("管理后台自有影片接口")
@allure.title("获取影片标准主M3U8-传入不存在的影片id")
@allure.description("传入不存在的影片id")
def test_originalvideo_standard_m3u8_002(login_start):
        token =login_start
        method=data["originalvideo_delete_alldefination"][1]["Method"]
        apiurl=data["originalvideo_delete_alldefination"][1]["ApiUrl"]
        response=send_requests(method,apiurl,token)
        # 断言
        assert response['code'] == '2005'
        assert response['message'] == '影片不存在'


if __name__ == '__main__':
    pytest.main(['-s',"test_selfvideo.py::test_modify_originalvideo001"])