import pymysql
import configparser

cf=configparser.ConfigParser()
cf.read("settings.ini")

db = pymysql.connect(cf.get('database', 'address'), cf.get('database', 'username'), cf.get('database', 'passwd'), cf.get('database', 'sqlname'))
cursor = db.cursor()
#execute = cursor.execute


def execute(str):
    db.ping(reconnect=True)
    cursor = db.cursor()
    return cursor.execute(str)


def sql_close():
    db.close()
    
    
def sql_commit():
    db.commit()
    

def get_points(qqid, groupid):
    n = execute('SELECT POINTS FROM points WHERE qqid = %d and groupid = %d' % (qqid,groupid))
    if(0 == n):
        execute('INSERT INTO points (qqid, groupid, points) values (%d, %d, 0)' % (qqid, groupid))
        db.commit();
        return 0;
    else:
        return cursor.fetchone()[0];
        

def set_points(qqid, groupid, value):
    n = execute('UPDATE points SET points = %d WHERE qqid = %d and groupid = %d' % (value, qqid, groupid))
    if(0 == n):
        execute('INSERT INTO points (qqid, groupid, points) values (%d, %d, 0)' % (qqid, groupid, value))
        db.commit();
    return n;
    

def add_points(qqid, groupid, value):
    n = execute('UPDATE points SET points = points + %d WHERE qqid = %d and groupid = %d' % (value, qqid, groupid))
    if(0 == n):
        execute('INSERT INTO points (qqid, groupid, points) values (%d, %d, %d)' % (qqid, groupid, value))
    db.commit()
    return n;


def minus_points(qqid, groupid, value):
    n = execute('UPDATE points SET points = points - %d WHERE qqid = %d and groupid = %d' % (value, qqid, groupid))
    if(0 == n):
        execute('INSERT INTO points (qqid, groupid, points) values (%d, %d, %d)' % (qqid, groupid, -value))
    db.commit();
    return n;





def literal_execute(args, groupid, qqid):
    if(not qqid == 2234748103):
        return "权限不足"
    elif not len(args) == 2: 
        return "参数错误"
    return str(eval(args[1]));

