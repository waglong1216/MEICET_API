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
     #获取