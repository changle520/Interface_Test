def replaceNone(d1):
    '''
    将字典中值为None的转换成空字符串
    :param d1: 传入一个字典类型的参数
    :return:
    '''
    params_dict={}
    for key,value in d1.items():
        if value==None:
            value=""
        params_dict[key]=value
    return params_dict

if __name__ == '__main__':
    print(replaceNone({"name":None,"age":None}))

