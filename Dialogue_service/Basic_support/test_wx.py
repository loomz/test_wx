# http://mp.weixin.qq.com/debug/cgi-bin/sandboxinfo?action=showinfo&t=sandbox/index
# appID: wx20d87c72dc1e93bf
# appsecret: deeced62d97f6ec9a53db64dd5dd1bf0

'''
测试内容：
１、测试开始获取access_token，只需要获取一次
２、测试结束打印　所有测试用例已完成
３、测试获取微信服务器IP地址方法；　测试用户管理　-> 获取用户列表、
４、测试用户分组　－>　标签管理：创建标签、获取公众号已创建的标签、编辑标签（修改标签）、删除标签
'''


import pytest
from common.common_read_file import CommonReadFile
from common.common_requests import CommonHttp



# 测试获取微信服务器IP地址方法
def test_api_domain_ip(token , http):
    token_id = token
    ip_url ='/get_api_domain_ip?access_token=%s' % token_id
    response_ip = http.get(ip_url)
    print('\n http状态码=%s, response.json=%s ' % (response_ip.status_code, response_ip.json()))
    assert response_ip.status_code == 200

