# coding=utf-8
import unittest


class AcctNameBatchCheck:
    def __init__(self, req, rsp, batch_no):
        self.req = req
        self.rsp = rsp
        self.batch_no = batch_no
        self.query_batch_info()

    def read_config(self):
        pass

    def query_batch_info(self):
        self.batch_no = 'OK'
        print (self.req, self.rsp, self.batch_no)

    def query_batch_detail(self):
        pass

    def generate_file(self):
        pass

    def get_file_content_and_insert_into_table(self):
        pass


class TestStringMethods(unittest.TestCase):
    def AcctNameBatchCheck(self):
        pass
