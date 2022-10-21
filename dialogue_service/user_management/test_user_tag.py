import json

import pytest
from common.common_read_file import CommonReadFile
from common.common_requests import CommonHttp


# 用户管理 /用户标签管理->创建标签
@pytest.mark.parametrize('tag_name,expect', CommonReadFile().get_data_json('test_user_tag_create.json'))
def test_create(tag_name, expect, token, http):
    url_tags_create ='/tags/create?access_token=%s' % token
    print('\n tag_name=%s' % tag_name)
    tags_data = {
        "tag": {"name": tag_name}
    }
    print('\n tags_data=%s' % tags_data)
    tags_response = http.post(url_tags_create, body=tags_data)
    print('\n http状态码=%s , response.json=%s' % (tags_response.status_code, tags_response.json()))
    if expect == 0:
        assert tags_response.status_code == 200 and "tag" in tags_response.json()
    else:
        assert tags_response.status_code == 200 and tags_response.json()['errcode'] == expect



#  获取公众号已创建的标签
def test_select(token, http):
    url_tag_select = '/tags/get?access_token=%s' % token
    tags_select_response = http.get(url_tag_select)
    # 打印出来的json格式的中文数据显示异常 ,json.dumps(tags_select_response.json(), ensure_ascii=False)
    tag_select_response_new = json.dumps(tags_select_response.json(), ensure_ascii=False)
    print('\n http状态码=%s,\n response.json=%s ' % (tags_select_response.status_code, tag_select_response_new))
    assert tags_select_response.status_code == 200 and "tags" in tags_select_response.json()


# 编辑标签
@pytest.mark.parametrize('tag_id,tag_name,expect', CommonReadFile().get_data_json('test_user_tag_update.json'))
def test_update(token, http, tag_id, tag_name, expect):
    url_tags_update ='/tags/update?access_token=%s' % token
    tags_data = {
            "tag": {"id": tag_id, "name": tag_name}
    }
    update_response = http.post(url_tags_update, body=tags_data)
    print('\n http状态码=%s, response.json=%s ' % (update_response.status_code, update_response.json()))
    if expect == 0:
        assert update_response.status_code == 200 and update_response.json()
    else:
        assert update_response.status_code == 200 and update_response.json()['errcode'] == expect


# 删除标签
@pytest.mark.parametrize('tag_id,expect', CommonReadFile().get_data_json('test_user_tag_delete.json'))
def test_delete(token, http, tag_id,expect):
    url_tags_delete ='/tags/delete?access_token=%s' % token
    tags_data = {
        "tag": {"id": tag_id}
    }
    delete_response = http.post(url_tags_delete, body=tags_data)
    print('\n http状态码=%s, response.json=%s ' % (delete_response.status_code, delete_response.json()))
    if expect == 0:
        assert delete_response.status_code == 200 and delete_response.json()
    else:
        assert delete_response.status_code == 200 and delete_response.json()['errcode'] == expect
