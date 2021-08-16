# -*- coding: utf-8 -*- 
# @Time : 2020/11/26 17:04 
# @Author : qian 
# @File : run.py
import pytest
from common.logger import Logging
import os
import logging

project_path = os.path.split(os.path.realpath(__file__))[0]
if ':' in project_path:
    project_path = project_path.replace('\\', '/')
else:
    pass
if __name__ == '__main__':
    Logging()
    # 定义测试集
    xml_report_path = project_path + '/Report/xml'
    html_report_path = project_path + '/Report/html'
    report = project_path + '/Report'
    args = ['--clean-alluredir', '-s', '-q', '--alluredir', xml_report_path]
    pytest.main(args)
    cmd = 'allure generate %s -o %s -c' % (xml_report_path,
                                           html_report_path)
    os.system(cmd)