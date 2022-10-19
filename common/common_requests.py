import requests
import json


# 定义一个common的类，它的父类是object
class CommonHttp(object):
    # common的构造函数
    def __init__(self, url_root):
        # 被测系统的根路由
        self.url_root = url_root

    # 封装你自己的get请求，uri是访问路由，params是get请求的参数，如果没有默认为空
    def get(self, uri, url_params=None, headers=None, cookies=None):
        # 拼凑访问地址
        url = self.url_root + uri
        # 通过get请求访问对应地址
        res = requests.get(url, params=url_params, headers=headers, cookies=cookies)
        # 返回request的Response结果，类型为requests的Response类型
        return res

    # 封装你自己的post方法，uri是访问路由，params是post请求需要传递的参数，如果没有参数这里为空
    def post(self, uri, url_params=None, body=None, headers=None, cookies=None):
        # 拼凑访问地址
        url = self.url_root + uri

        default_headers = {"Content-Type": "application/json; charset=UTF-8"}
        all_headers = default_headers if headers is None else {**default_headers, **headers}

        body = json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None
        response = requests.post(url, params=url_params, data=body, headers=all_headers, cookies=cookies)

        return response
