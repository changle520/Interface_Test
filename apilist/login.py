
import logging
from common.request import Request
from common.logger import Logging
from common.generateSignature import get_sign
from common.hashlibSHA1 import get_str_sha1
from conf.meiziku import url,username,password,headers_conf
Logging()

rq=Request()

def login(**kwargs):
    login_api="manager/v1/user/login"
    login_url="{}/{}".format(url,login_api)
    headers = headers_conf

    #获取sign
    heaerws_signature=get_sign(**kwargs)
    #拼接请求头
    headers.update(heaerws_signature)
    print(headers)

    print(kwargs)
    #发送请求
    try:
        response=rq.request('POST',login_url,headers=headers,data=kwargs).json()
        if 'value' in response.keys():
            token=response["value"]['userTokenResponse']['token']
            rlt={"response":response,"token":token}
        else:
            rlt = {"response": response}
        return rlt
    except Exception as error:
        logging.info("登录不成功:{}".format(error))


if __name__ == '__main__':
    password=get_str_sha1(password)
    params={"username":username,"password":password}
    print(login(**params))


