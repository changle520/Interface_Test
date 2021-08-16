import hashlib
import base64

'''
客户端用户密码加密规则
1、明码 + salt（salt：w1fsd2DurO0）
2、做sha1加密，获取16进制字符串
3、做base64编码，UTF-8格式
'''

def get_str_sha1(strvalue):
    '''
    对密码进行sha1加密
    :param strvalue: 要加密的字符串
    :return: 返回加密后的内容
    '''
    if not strvalue:
        strvalue=''
        return strvalue
    #给明文密码加盐
    strvalue=str(strvalue)+'w1fsd2DurO0'
    #进行sha1()加密
    sha = hashlib.sha1(strvalue.encode('utf-8'))
    encrypts = sha.hexdigest()
    #将16进制字符串进行base64编码
    encrypts_base64=base64.b64encode(encrypts.encode('utf-8'))
    encrypts_str=str(encrypts_base64,'utf-8')
    return encrypts_str


get_str_sha1('123456789')

