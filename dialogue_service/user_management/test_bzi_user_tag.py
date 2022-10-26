import json
import pytest
from common.common_read_file import CommonReadFile
from common.common_requests import CommonHttp


# 用户管理 /用户标签管理->创建标签
def addTag(http, token):
    url_tags_create ='/tags/create?access_token=%s' % token
    tag_name ='test01i'
    tags_data = {
        "tag": {"name": tag_name}
    }
    print('\n tags_data=%s' % tags_data)
    tags_response = http.post(url_tags_create, body=tags_data)
    print('\n http状态码=%s , response.json=%s' % (tags_response.status_code, tags_response.json()))
    print('创建标签成功:\n', tags_response.json())
    if tags_response.json()['tag']['name'] == tag_name :
        assert tags_response.status_code == 200 and "tag" in tags_response.json()
    else:
        assert tags_response.status_code == 200 and tags_response.json()


def updateTag(http, token,tag_id,tag_name):
    url_tags_update = '/tags/update?access_token=%s' % token
    tags_data = {
        "tag": {"id": tag_id, "name": tag_name}
    }
    update_response = http.post(url_tags_update, body=tags_data)
    print('\n http状态码=%s, response.json=%s ' % (update_response.status_code, update_response.json()))
    errcode = update_response.json()['errcode']
    if errcode == 0:
        assert update_response.status_code == 200 and update_response.json()
    else:
        assert update_response.status_code == 200 and update_response.json()['errcode'] == errcode

def deleteTag(token, http, tag_id):
    url_tags_delete ='/tags/delete?access_token=%s' % token
    tags_data = {
        "tag": {"id": tag_id}
    }
    delete_response = http.post(url_tags_delete, body=tags_data)
    print('\n http状态码=%s, response.json=%s ' % (delete_response.status_code, delete_response.json()))
    errcode = delete_response.json()['errcode']
    if errcode == 0:
        assert delete_response.status_code == 200 and delete_response.json()
    else:
        assert delete_response.status_code == 200 and delete_response.json()['errcode'] == errcode

def getTag(token, http):
    url_tag_select = '/tags/get?access_token=%s' % token
    tags_select_response = http.get(url_tag_select)
    # 打印出来的json格式的中文数据显示异常 ,json.dumps(tags_select_response.json(), ensure_ascii=False)
    # tag_select_response_new = json.dumps(tags_select_response.json(), ensure_ascii=False)
    print('\n http状态码=%s,\n response.json=%s ' % (tags_select_response.status_code, tags_select_response.json()))
    assert tags_select_response.status_code == 200 and "tags" in tags_select_response.json()
    tag_id =tags_select_response.json()['tags'][5]['id']
    print('查询tag_id=%s\n' % tag_id)


def test_get_tag(http,token):
    tag_id = getTag(token, http)
    deleteTag(http,token,tag_id)



