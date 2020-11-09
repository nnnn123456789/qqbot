from database import *;

#-2 (global block list)
#-1 (group block list)
#0 (common user)
#1 (named)
#2 (group white list)
#3 (global white list)
#4 (labeled  群主头衔)
#5 (group lower manager)
#6 (global lower manager)
#7 (group manager)
#8 (group higher manager)
#9 (global higher namager)
#10 (bot manager)
#11 (group owner)
#12 (bot owner)


def get_global_authlevel(qqid):
    n = execute('SELECT level FROM user_level WHERE qqid = %d and groupid = 0' % (qqid))
    if(0 == n):
        execute('INSERT INTO user_level (qqid, groupid, level) values (%d, 0, 0)' % (qqid))
        db.commit();
        return 0;
    else:
        return cursor.fetchone()[0];
        

def get_local_authlevel(qqid, groupid):
    n = execute('SELECT level FROM user_level WHERE qqid = %d and groupid = %d' % (qqid, groupid))
    if(0 == n):
        execute('INSERT INTO user_level (qqid, groupid, level) values (%d, %d, 0)' % (qqid, groupid))
        db.commit();
        return 0;
    else:
        return cursor.fetchone()[0];
        

def get_authlevel(qqid, groiupid):
    gl = get_global_authlevel(qqid);
    lo = get_local_authlevel(qqid, groupid);
    if(gl == 0 or lo == 0):
        return gl + lo;
    else:
        return max(gl,lo);


def set_global_authlevel(qqid, level):
    n = execute('SELECT level FROM user_level WHERE qqid = %d and groupid = 0' % (qqid))
    if(0 == n):
        execute('INSERT INTO user_level (qqid, groupid, level) values (%d, 0, %d)' % (qqid, level))
    else:
        execute('UPDATE user_level SET level = %d WHERE qqid = %d and groupid = 0' % (level, qqid))
    db.commit();
    return n;
    

def set_local_authlevel(qqid, groupid, level):
    n = execute('SELECT level FROM user_level WHERE qqid = %d and groupid = %d' % (qqid, groupid))
    if(0 == n):
        execute('INSERT INTO user_level (qqid, groupid, level) values (%d, %d, %d)' % (qqid, groupid, level))
    else:
        execute('UPDATE user_level SET level = %d WHERE qqid = %d and groupid = %d' % (level, qqid, groupid))
    db.commit();
    return n;
    


       
        
        
        