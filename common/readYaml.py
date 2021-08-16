import yaml
import os
import os.path
import logging
from common.logger import Logging
Logging()
class ReadFileData():
    def __init__(self):

        pass

    def load_yaml(self, file_path):
        with open(file_path, encoding = 'UTF-8') as f:
            data = yaml.safe_load(f)
        logging.info("读到数据 ==>>  {} ".format(data))
        return data

    def get_data(self,path,yaml_file_name):
        try:
            data_file_path = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '/' + path+ '/' + yaml_file_name
            yaml_data = self.load_yaml(data_file_path)
        except Exception as ex:
            print(ex)
            logging.error(ex)
        else:
            return yaml_data
data = ReadFileData()

if __name__ == '__main__':
    ReadFileData=ReadFileData()
    dat = ReadFileData.get_data('test_data/ParamYaml','meiziku_api.yml')
    print(dat)

