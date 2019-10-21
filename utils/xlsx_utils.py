'''
从Excel获取测试用例相关数据
'''
import xlrd,logging

def get_test_xlsx(filepath,index):
    try:
        file = xlrd.open_workbook(filepath)
        tmp = file.sheets()[index]
        nrows = tmp.nrows
        listdata = []
        for i in range(1, nrows):
            dict_param = {}
            dict_param['id']=tmp.cell(i, 0).value
            dict_param['model']=tmp.cell(i, 1).value
            dict_param['logout']=(tmp.cell(i, 2).value)
            dict_param.update(eval(tmp.cell(i, 3).value))
            dict_param.update(eval(tmp.cell(i, 4).value))
            listdata.append(dict_param)
        return listdata
    except Exception as e:
        logging.warning('获取测试用例参数失败！失败原因：%s'%e) #log
        return e