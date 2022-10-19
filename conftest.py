import pytest
from common.common_read_file import CommonReadFile
from common.common_requests import CommonHttp

comm = CommonHttp('https://api.weixin.qq.com/cgi-bin')

#获取token
@pytest.fixture(scope='session', name='token')
def access_token():
    APPID = 'wx20d87c72dc1e93bf'
    APPSECRET = 'deeced62d97f6ec9a53db64dd5dd1bf0'
    token_url = '/token?grant_type=client_credential&appid=%s&secret=%s' % (APPID, APPSECRET)
    response_token = comm.get(token_url)
    print('http状态码=%s, response.json=%s ' % (response_token.status_code, response_token.json()))
    # print('token=%s' % response_token.json()['access_token'])
    token =response_token.json()['access_token']
    assert response_token.status_code == 200
    yield token
    print('\n所有测试用例已完成================>')