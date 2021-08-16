import json
from json import JSONDecodeError
from tool.replaceRelevance import replace
import os
def read_data(param, relevance=None):
    """
    读取用例中参数data
    :param relevance: 关联对象
    :param param: 用例中data
    :return:
    """
    _path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    if isinstance(param, dict):
        param = replace(param, relevance)
    elif isinstance(param, list):
        param = replace(param, relevance)
    elif param is None :
        pass
    elif isinstance(param,str) and  len(param) <=0 :
        pass
    elif isinstance(param,str) and  len(param) >0 and param.find(".json") < 0:
        param = json.loads(param)
    else:
        try:
            _path=str(_path) + '/test_data/ParamYaml/' + param
            with open(_path, encoding='UTF-8') as f:
                param = json.load(f)
                # for i in data:
                #     param = i["parameter"]
                #     break

                if not isinstance(param, dict):
                    raise Exception("未能找到用例关联的参数\n文件路径：%s\n索引：%s" % (param, _path))
                else:
                    param = replace(param, relevance)
        except FileNotFoundError:
            raise Exception("用例关联文件不存在\n文件路径： %s" % param)
        except JSONDecodeError:
            raise Exception("用例关联的参数文件有误\n文件路径： %s" % param)
    return param

if __name__ == '__main__':
    read_data('registerFromThirdPart.json')