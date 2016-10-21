#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import tornado.web
import tornado
import json


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        data = requests.get("http://www.servicefarsi.com/api/news/9770847265091/4/item=0,page=1/")
        data = json.loads(data.text)
        data_res = data['res']

        data2 = requests.get("http://www.servicefarsi.com/api/news/9770847265091/4/item=19,type=0,page=1/")
        data2 = json.loads(data2.text)
        data2_res = data2['res']


        self.render('index.html', title="index",data = data_res, data2 = data2_res)

    def post(self, *args, **kwargs):
        # amount = self.get_argument('amount')
        self.write('success')
