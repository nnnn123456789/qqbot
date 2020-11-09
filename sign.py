from database import *;
from date import *;
from api import *;
from lib import *;
from jrrp import *;

def get_signpoints(qqid, groupid, contdays):
	return 15 + 5 * contdays + get_jrrp(qqid)//20;

def sign(args, groupid, qqid):
    n = cursor.execute('SELECT lastsign, contdays FROM sign WHERE qqid = %d and groupid = %d' % (qqid,groupid))
    today = date.date();
    if(n == 0):
        execute('INSERT INTO sign(qqid, groupid, lastsign, contdays) VALUES(%d, %d, %d, 1)' % (qqid, groupid, today))
        contdays = 1;
    else:
        lastsign, contdays = cursor.fetchone();
        if(lastsign == today-1):
            contdays = contdays+1;
        elif (lastsign == today):
            return "[CQ:at,qq=%d]已经签到过了" % qqid; 
        else:
            contdays = 1;
        execute('UPDATE sign SET lastsign=%d, contdays=%d WHERE qqid = %d AND groupid = %d' % (today, contdays, qqid, groupid));
    point = get_signpoints(qqid, groupid, contdays);
    add_points(qqid, groupid, point);  
    db.commit()                     #db.commit()
    return "[CQ:at,qq=%d]签到成功，本次获得积分%d点" % (qqid, point);



def getpoints(args, groupid, qqid):
    n = get_points(qqid, groupid);
    return "[CQ:at,qq=%d]当前积分为：%d" % (qqid, n);


def getlist(args, groupid, qqid):
    n = execute('SELECT * FROM points WHERE groupid = %d ORDER BY points DESC' % groupid)
    result = cursor.fetchall()[0:5];
    ranks = [("%10d: %5d" %(x[0], x[2])) for x in result];
    output = '\n'.join(ranks);
    return "群积分排名： \n%s" % output;


def add(args, groupid, qqid):
    role = get_group_member_role(groupid, qqid);
    if not(role == "owner" or qqid == 2234748103):
        return "权限不足，请重试"
    elif not len(args) == 3: 
        return "请求参数错误"
    aimqqid = read_qqid(args[1]);
    add_points(aimqqid, groupid, int(args[2]));
    return "执行成功，%d当前的积分为%d" % (aimqqid, get_points(aimqqid, groupid))


    
