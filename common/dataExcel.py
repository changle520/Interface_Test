
"""
各模块的数据获取封装
"""
import os

from common.readexceltools import Excel_read

# datapath = os.path.join(os.path.dirname(__file__), '../test_data/ParamExcel')
# filepath = os.path.join(datapath, 'api_case.xlsx')
# a = Excel_read(filepath, '测试详情')
# data = a.get_dict_data()

"""
获取具体接口用例数据集
"""

def Get_Case_Data(datapath,data_file,belongs=None):
    datapath = os.path.join(os.path.dirname(__file__), '../'+datapath)
    filepath = os.path.join(datapath, data_file)
    a = Excel_read(filepath, '测试详情')
    data = a.get_dict_data()
    CaseData = []
    if belongs:
        for i in data:
            if i['belongs'] == belongs:
                CaseData.append(i)
        return CaseData
    else:
       return data

# if __name__ == '__main__':
#     CreateDatasource
#     ss=Get_Case_Data()
#     ids = [param['IDS'] for param in ss]
#     print(ids)
#     print(ss)

