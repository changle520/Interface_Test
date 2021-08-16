import hashlib, hmac, base64
from urllib import parse
from conf.meiziku import accessSecret,accessKey

'''
参数签名生成方式：
参数 = access-key加所有非header参数
按照key的字典顺序来排序（升序）
签名采用HmacSHA1算法 + Base64，编码采用：UTF-8参考过程如下:

例：
access-key:test1111
access-secret:s111111

access-key: ZtOFebmB
access-secret: 73f26e690eae141345591bef933f86092449cbcb

初始参数
payFlowNo=9210629634560088&apple=p1&test=p2&baidu=p3

1所有参数加access-key，按照参数名，的字典顺序来排序(升序)
access-key=test1111&apple=p1&baidu=p3&payFlowNo=9210629634560088&test=p2
2刚刚的字符串，转换为url编码格式
access-key%3Dtest1111%26apple%3Dp1%26baidu%3Dp3%26payFlowNo%3D9210629634560088%26test%3Dp2
access-key%3Dtest1111%26apple%3Dp1%26baidu%3Dp3%26payFlowNo%3D9210629634560088%26test%3Dp2
3使用系统分配的access-key，通过HmacSHA1+Base64后
rzxDuaCPOkoG96PiGa8cKAGLcaw=
'''
'''
url编码：
poet_name = "&&changle"
#将字符串转换成url编码
url_code_name = parse.quote(poet_name)
print(url_code_name)

#将url编码进行解码
unurl_code_name = parse.unquote(poet_name)
print(unurl_code_name)
'''

def get_sign(**kwargs):
    #将access-key初始化到存储参数的字典对象中
    params_key={"access-key":accessKey}
    #将入参添加到参数字典对象中
    params_key.update(kwargs)
    params = []
    #将参数根据首字母排序并格式化
    for key, value in sorted(params_key.items()):
        if value==None:
            value=""
        params.append("{}={}".format(key,value))
    params='&'.join(params)
    #将格式化后的参数进行url编码
    url_params=parse.quote(params,safe='')  # safe的值不会转义  /默认不转义，如果要转义可设置safe=''
    # print(url_params)
    #hmac加密
    hmac_url_params=hmac.new(bytes(accessSecret, 'utf-8'), bytes(url_params, 'utf-8'), hashlib.sha1).digest()
    #base64加密并
    base_url_params=base64.b64encode(hmac_url_params)
    #转换成字符串
    sign=str(base_url_params,'utf-8')
    #拼接请求头参数
    headers={"access-key":accessKey,"signature":sign}
    return headers
if __name__ == '__main__':
    data = {"payFlowNo":"9210629634560088","apple":"p1","test":"p2","baidu":"p3","access-key":"test1111"}
    print(get_sign(apple="p1",baidu="p3",payFlowNo="9210629634560088",test="p2"))

