from common.config_handler import ConfigHandler,config
from setting.constant import p_path
from common.logger_handler import LoggerHandler
from common.requests_handler import RequestsHandler
from common.excel_handler import ExcelHandler
from libs.ddt import ddt,data
import unittest
import os

''''
@ddt
class TestLogin(unittest.TestCase):
     #配置文件读取Excel文件名
     file_name = config.read("excel","file_name")
     #拼接Excel的路径
     file_path = os.path.join(p_path.DATA_PATH,file_name)
     #读取Excel表单名
     sheet_name = config.read("excel","login_sheet")
     #读取url
     base_url = config.read("http","base_url")
     login_url = config.read("http","login_url")
     url = base_url  + login_url

     #读取headers
     header = config.read("http","headers")
     #获取Excel中的数据
     test_data =ExcelHandler2(file_path).read(sheet_name)

     @classmethod
     def setUpClass(cls) -> None:
         cls.req = RequestsHandler()

     @classmethod
     def tearDownClass(cls) -> None:
         pass

     def setUp(self):
         pass

     def tearDown(self):
         pass


     @data(*test_data)
     def test_login(self,test_info):
         res = self.req.json(test_info['method'],
                             self.url,
                             json=test_info['data'],
                             headers=eval(self.header))
         print(res)'''
@ddt
class TestLogin(unittest.TestCase):
    # 读取配置文件
    file_name = config.read('excel', 'file_name')
    file_path = os.path.join(p_path.DATA_PATH, file_name)
    # Excel 表格名称
    sheet_name = config.read('excel', 'login_sheet')
    # url 地址
    url = config.read('http', 'base_url')
    # 读取 headers 信息
    headers = config.read('http', 'headers')

    excel_sheet = ExcelHandler(file_path,sheet_name)
    test_data = excel_sheet.read()

    @classmethod
    def setUpClass(cls):
        cls.req = RequestsHandler()

    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*test_data)
    def test_login(self, test_info):
        # 调用 requests 模块访问接口
        # test_info['data'] = replace_label(test_info['data'])

        res = self.req.json(test_info["method"],
                            self.url + test_info["url"],
                            json=eval(test_info["data"]),
                            headers=eval(self.headers))
        print(res)
        self.assertEqual(test_info["expected"],eval(res["code"]))
