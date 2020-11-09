import requests;
import json;


host_addr = 'http://127.0.0.1:5700/'


def send_private_msg (user_id, message, auto_escape=False):
	url = host_addr + 'send_private_msg'
	d = {'user_id':user_id,'message': message,'auto_escape': auto_escape}
	r = requests.post(url, data=d)
	return json.loads(r.text)["data"]


def send_group_message(group_id, message, auto_escape=False):
    url = host_addr + 'send_group_msg'
    d = {'group_id':group_id,'message': message,'auto_escape': auto_escape}
    r = requests.post(url, data=d)
    return json.loads(r.text)["data"]


def send_discuss_message(discuss_id, message, auto_escape=False):
    url = host_addr + 'send_group_msg'
    d = {'discuss_id':discuss_id,'message': message,'auto_escape': auto_escape}
    r = requests.post(url, data=d)
    return json.loads(r.text)["data"]


def get_group_member_info(groupid, qqid, nocache=False):
    url = host_addr + 'get_group_member_info'
    d = {'group_id':groupid, 'user_id':qqid,'no_cache':nocache}
    r = requests.post(url, data=d)
    return json.loads(r.text)["data"]

# "owner" "admin" "member"
def get_group_member_role(groupid, qqid):
    data = get_group_member_info(groupid, qqid);
    print(data);
    return data["role"]


def set_group_ban(qqid, groupid, duration):
    url = host_addr + 'set_group_ban'
    d = {'group_id':groupid,'user_id': qqid,'duration': duration}
    r = requests.post(url, data=d)
    return json.loads(r.text)["data"]




