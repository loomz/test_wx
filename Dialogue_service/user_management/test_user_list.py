import pytest
from common.common_read_file import CommonReadFile
from common.common_requests import CommonHttp



#获取用户列表
def test_user_list(token,http):
    #print('access_token=%s' % token_id)
    user_list_select ='/user/get?access_token=%s' % token
    # print('tags_data=%s' % user_list_select)
    select_response = http.get(user_list_select)
    print('\n http状态码=%s, response.json=%s ' % (select_response.status_code, select_response.json()))
    assert select_response.status_code == 200 and select_response.json()['total'] == 2


