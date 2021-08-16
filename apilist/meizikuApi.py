import logging
from common.logger import Logging
from common.request import Request
from common.hashlibSHA1 import get_str_sha1
from common.generateSignature import get_sign
from common.dict_replaceNone import replaceNone
from apilist.login import login
from conf.meiziku import url,username,password,headers_conf

Logging()

rq=Request()

def send_requests(method,api,token,headers=None,params=None,data=None):
    '''
    发送接口请求，通用方法
    :param api:接口api
    :param method:请求方法
    :param headers:请求头
    :param params:请求参数
    :param kwargs:请求参数
    :return:返回接口的响应结果
    '''
    url_api = "{}/{}".format(url,api)
    if headers == None:
        headers={"token":token}
    else:
        headers.update({"token":token})

    # 获取sign
    if params:   #如果请求接口传的参数是拼在url后面的,生成签名的方法中传入params
        heaerws_signature = get_sign(**params)
    elif data:
        heaerws_signature = get_sign(**data) #如果请求接口传的参数是在请求体中,生成签名的方法中传入kwargs
    else:   #如果没有请求参数,传空
        heaerws_signature=get_sign(**{})

    # 拼接请求头
    headers.update(heaerws_signature)
    logging.info("请求头:{}".format(headers))

    #将入参字典中的None替换成空字符串
    if params:
        params=replaceNone(params)
    if data:
        data=replaceNone(data)
    # 发送请求
    response = rq.request(method,url_api,headers=headers, params=params,data=data).json()
    return response


if __name__ == '__main__':
    password=get_str_sha1(password)
    token=login(username=username,password=password)["token"]
    # send_requests('GET',"manager/v1/originalvideo/list",token,q='123',page=1,size=10,videoFormatKey="",playerFormatKey="",sortField="",sort="")
    # send_requests('GET',"manager/v1/originalvideo/list",token,q='123',page=1,size=10,videoFormatKey=None,playerFormatKey=None,sortField=None,sort=None)

    # send_requests('GET', "manager/v1/access/appkey",token, q='浙江露熙')
    send_requests('POST', "manager/v1/access/appkey", token, name='测试用33')
    # send_requests('DELETE', "manager/v1/access/appkey", token, id='1536427590712168448')








