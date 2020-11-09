from api import *

import requests;
import json;
import autoreply
import lib
import echo
import jrrp
import sign
import database;
import sleep;

group_ans_pool = {};
group_ans_pool["#echo"] = echo.echo
group_ans_pool["#添加自动回复"] = autoreply.add_auto_reply
group_ans_pool["#jrrp"] = jrrp.jrrp
group_ans_pool["#签到"] = sign.sign
group_ans_pool["#积分查询"] = sign.getpoints
group_ans_pool["#积分排名"] = sign.getlist
group_ans_pool["#加分"] = sign.add
group_ans_pool["#执行"] = database.literal_execute
group_ans_pool["#sleep"] = sleep.sleep

def on_group_message(m):
	print("原始文本： " + m["raw_message"])
	autoans = autoreply.get_autoans(m["raw_message"])
	if not autoans == "":
		send_group_message(m["group_id"],  autoans)
	args = lib.div_args(m["raw_message"])
	#print(args[0])
	cmd = group_ans_pool.get(args[0])
	#print(cmd)
	if not cmd == None:
		ans = cmd(args, m["group_id"], m["user_id"])
		if not ans == "":
			send_group_message(m["group_id"], ans);
	pass;


def on_private_message(m):
	pass;


def on_group_manager_change(m):
	pass;


def on_group_users_add(m):
	ret = send_group_message(m["group_id"], "欢迎新同学[CQ:at,qq=%ld]，改个群名片，向大家介绍一下自己吧" % int(m["user_id"]));
	set_group_ban(m["user_id"], m["group_id"], 5 * 60);
	print("欢迎成功");
	


def on_group_users_delete(m):
	#ret = send_group_message(m["group_id"], "成员%d已退出该群" % int(m["user_id"]));
	#print(ret);
	print("人员离群");
	pass;


def on_group_ban(m):
	pass;


def on_group_document_upload(m):
	pass;


def on_request_friend_add(m):
	pass;


def on_request_group_invite(m):
	pass;


def on_group_message_recall(m):
	msg = ""
	if(m["user_id"] == m["operator_id"]):
		msg = "[CQ:at,qq=%ld]不许撤回，我看到啦！" % m["user_id"];
		return;
	else:
		return;
	ret = send_group_message(m["group_id"], msg);
	print(ret);
	pass;


def on_private_message_recall(m):
	pass;
