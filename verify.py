# coding=utf-8

import re
import A_Tools
import unittest


def amount_check(amount):
    if type(amount) is not str:
        return False
    reg_ex = re.compile(r"^([1-9]\d{0,9}|0)(\.\d{1,2})?$")
    return bool(reg_ex.match(amount))


def bank_account_strict_check(account):
    try:
        return sum(map(
            lambda (i, v):
            int(v) * 2 / 10 + int(v) * 2 % 10
            if i % 2 == 0
            else int(v),
            enumerate(account)
        )) % 10 == 0
    except ValueError:
        return False
    except TypeError:
        return False


def bank_account_check(account):
    if type(account) is not str:
        return False
    reg_ex = re.compile(r"^[1-9]\d{9,29}$")
    return bool(reg_ex.match(account))


def chinese_name_check(name, encoding="UTF-8"):
    if type(name) is not str:
        return False
    reg_ex = re.compile(ur"^(?!·)(?!.*(·)\1+).*[\u4e00-\u9fa5·]{2,16}(?<!·)$")
    return bool(reg_ex.match(unicode(name, encoding)))


def id_no_check(id_no):
    if len(str(id_no)) != 18:
        return False
    factor = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    last = ("1", "O", "X", "9", "8", "7", "6", "5", "4", "3", "2")
    id_no = str(id_no)

    each_digit_sum = 0
    for i in range(0, 17):
        try:
            each_digit_sum += int(id_no[i]) * factor[i]
        except ValueError:
            return False
    each_digit_sum %= 11
    return (last[each_digit_sum]) == str(id_no[17])


class TestStringMethods(unittest.TestCase):
    def test_verify_or_a_tools(self):
        account = 6214839919313330
        print(bank_account_strict_check(account))

        account_list = ["6214839919313330"]
        for i, v in enumerate(account_list):
            if not bank_account_check(v):
                raise Exception("第%s个账号验证失败" % (i + 1))

        chinese_name = 34
        print(chinese_name_check(chinese_name))

        id_no = "5002341996X909633"
        print(id_no_check(id_no))

        source_str = "32"
        print(A_Tools.insert_after_han(source_str))

        filename = "mine_info.ini"
        options = A_Tools.read_config_file(filename)
        print(options.items("wiki"))

        amount = 0.235
        print (amount_check(amount))

        print(A_Tools.format_amount(amount))
