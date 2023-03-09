import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_dir = os.path.join(root_dir, 'config')
data_dir = os.path.join(config_dir, 'data.yaml')
print(data_dir)
