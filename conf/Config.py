
import configparser
import os

from configparser import ConfigParser
from common.logger import Logging
import logging



class Config:
    # titles:
    TITLE_EVN = "evn"
    TITLE_EMAIL = "mail"
    TITLE_DB="DB_config"

    # values:
    # [evn]
    VALUE_TESTER = "tester"
    VALUE_ENVIRONMENT = "environment"
    VALUE_VERSION_CODE = "versionCode"
    VALUE_HTTP_TYPE="http_type"
    VALUE_HOST = "host"
    VALUE_PORT= "port"
    VALUE_LOGIN_INFO = "loginInfo"
    VALUE_LOGIN_HOST = "loginHost"

    # [mail]
    VALUE_SMTP_SERVER = "smtpserver"
    VALUE_SENDER = "sender"
    VALUE_RECEIVER = "receiver"
    VALUE_USERNAME = "username"
    VALUE_PASSWORD = "password"

    # [DB]
    VALUE_DB_USER="user"
    VALUE_DB_PASSWORD="passwd"
    VALUE_DB_LISTENER="listener"

    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        Logging()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.xml_report_path = Config.path_dir+'/Report/xml'
        self.html_report_path = Config.path_dir+'/Report/html'

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(self.conf_path, encoding='gbk')


        self.tester_release = self.get_conf(Config.TITLE_EVN, Config.VALUE_TESTER)
        self.environment_release = self.get_conf(Config.TITLE_EVN, Config.VALUE_ENVIRONMENT)
        self.versionCode_release = self.get_conf(Config.TITLE_EVN, Config.VALUE_VERSION_CODE)
        self.http_type_release=self.get_conf(Config.TITLE_EVN,Config.VALUE_HTTP_TYPE)
        self.host_release = self.get_conf(Config.TITLE_EVN, Config.VALUE_HOST)
        self.port_release = self.get_conf(Config.TITLE_EVN, Config.VALUE_PORT)
        self.loginInfo_release = self.get_conf(Config.TITLE_EVN, Config.VALUE_LOGIN_INFO)
        self.loginHost_release = self.get_conf(Config.TITLE_EVN, Config.VALUE_LOGIN_HOST)

        self.smtpserver = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SMTP_SERVER)
        self.sender = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SENDER)
        self.receiver = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_RECEIVER)
        self.username = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_USERNAME)
        self.password = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_PASSWORD)

        self.db_user = self.get_conf(Config.TITLE_DB, Config.VALUE_DB_USER)
        self.db_password = self.get_conf(Config.TITLE_DB, Config.VALUE_DB_PASSWORD)
        self.db_listenter = self.get_conf(Config.TITLE_DB, Config.VALUE_DB_LISTENER)

    def read_dir(self):
        """
        读取配置文件中directory相关信息
        :return:
        """
        self.config.read(self.conf_path, encoding='utf-8')
        directory = self.config['directory']
        return directory

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

if __name__ == '__main__':
    CONF=Config()
    print(CONF.TITLE_EVN)
    # CONF.add_conf('Session')
    #CONF.set_conf('Session','session',"1111")
    ss=CONF.get_conf('Session','session')
    print(ss)
