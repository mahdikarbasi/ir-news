#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import tornado.web
import tornado
import json


class NewsHandler(tornado.web.RequestHandler):
    def get(self,*args, **kwargs):

        url = "http://www.servicefarsi.com/api/news/9770847265091/7/item=" + args[0]
        data = requests.get(url)
        data = json.loads(data.text)
        data_res = data['res']

        self.render('news.html',data_res = data_res)

    def post(self, *args, **kwargs):
        # amount = self.get_argument('amount')
        self.write('success')
