# coding=utf-8
import re

import ConfigParser

from decimal import Decimal


# 金额格式化
def format_amount(amount):
    return "{:.2f}".format(Decimal(amount))


class CaseSensitiveRawConfigParser(ConfigParser.RawConfigParser):
    def optionxform(self, optionstr):
        return optionstr


# 读取ini配置文件,key值区分大小写
def read_config_file(filename, section=None):
    config = CaseSensitiveRawConfigParser(dict_type=dict)
    config.read(filename)
    if section:
        return config.items(section)
    else:
        return config


# 在汉字之后,字母或数字之前插入
def insert_after_han(source_string, inserted_string="|", coding="UTF-8"):
    reg_ex = re.compile(ur"(?<=[⺀-⺙⺛-⻳⼀-⿕々〇〡-〩〸-〺〻㐀-䶵一-鿃豈-鶴侮-頻並-龎])(?=[a-zA-Z\d])")
    return reg_ex.sub(unicode(inserted_string, coding), unicode(source_string, coding))
