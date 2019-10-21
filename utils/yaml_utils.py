import os,yaml

def open_yaml(path):
    try:
        file = open(r'%s'%path, 'r', encoding='utf-8')
        data = yaml.load(file)
        return {'code': 0, 'data': data}
    except Exception as e:
        print("yaml文件解析失败，原因%s"%e)
        return {'code': 1,'data': e}

def locate_yaml(str):
    path = os.getcwd() + '/data/location/' + str.lower() + '.yaml'