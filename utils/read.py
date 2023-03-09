import configparser
import os

import yaml

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_dir = os.path.join(root_dir, 'data')
data_path = os.path.join(config_dir, 'data.yaml')
config_dir = os.path.join(root_dir, 'config')
settings_path = os.path.join(config_dir, 'settings.ini')


class FileRead:
    def __init__(self):
        self.data_path = data_path
        self.ini_path = settings_path

    def read_data(self):
        with open(self.data_path, encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data

    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(self.ini_path)
        return config

base_data = FileRead()
print(base_data.read_data()['mobile_belong'])