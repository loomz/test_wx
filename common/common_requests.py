import requests
import json


# 定义一个common的类，它的父类是object
class CommonHttp(object):
    # common的构造函数
    def __init__(self, url_root, url_params=None, headers=None, cookies=None):
        # 被测系统的根路由
        self.url_root = url_root
        self.url_params = url_params

        default_headers = {"Content-Type": "application/json; charset=UTF-8"}
        self.headers = default_headers if headers is None else {**default_headers, **headers}

        self.cookies = cookies

    # 封装你自己的get请求，uri是访问路由，params是get请求的参数，如果没有默认为空
    def get(self, uri, url_params=None, headers=None, cookies=None):
        # 拼凑访问地址
        url = self.url_root + uri

        all_url_params = self.__build_url_params(url_params)
        all_headers = self.__build_headers(headers)

        # 通过get请求访问对应地址
        res = requests.get(url, params=all_url_params, headers=all_headers, cookies=cookies)
        # 返回request的Response结果，类型为requests的Response类型
        return res

    # 封装你自己的post方法，uri是访问路由，params是post请求需要传递的参数，如果没有参数这里为空
    def post(self, uri, url_params=None, body=None, headers=None, cookies=None):
        # 拼凑访问地址
        url = self.url_root + uri

        all_url_params = self.__build_url_params(url_params)
        all_headers = self.__build_headers(headers)
        body = json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None

        response = requests.post(url, params=all_url_params, data=body, headers=all_headers, cookies=cookies)

        return response

    def __build_url_params(self, url_params):
        if self.url_params is not None and url_params is None:
            all_url_params = self.url_params
        elif url_params is not None and self.url_params is None:
            all_url_params = url_params
        elif self.url_params is not None and url_params is not None:
            all_url_params = {**self.url_params, **url_params}

        print("all_url_params=%s" % all_url_params)

        return all_url_params

    def __build_headers(self, headers):
        all_headers = self.headers if headers is None else {**self.headers, **headers}
        print("all_headers=%s" % all_headers)
        return all_headers
