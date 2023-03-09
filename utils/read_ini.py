import configparser
import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_dir = os.path.join(root_dir, 'config')
settings_dir = os.path.join(config_dir, 'settings.ini')


def read_ini():
    config = configparser.ConfigParser()
    config.read(settings_dir)
    return config


print(read_ini()['host']['juhe_api_host'])
