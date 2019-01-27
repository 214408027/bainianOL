import yaml
import os

# 读取yaml数据
def read_yaml_data(file_name):
    with open('./data' + os.sep + file_name, 'r', encoding='utf-8') as f:
        return yaml.load(f)


# 读取yaml数据
# def get_data():
#     data = read_yaml_data('sms_send.yaml')
#     return data.get('send_data')