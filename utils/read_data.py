import os

import yaml

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_dir = os.path.join(root_dir, 'data')
data_dir = os.path.join(config_dir, 'data.yaml')


def read_data(filename):
    with open(filename, encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data


get_data = read_data(data_dir)
print(get_data['mobile_belong'])
