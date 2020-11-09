import date

def get_jrrp(qqid):
    s = str(date.date()) + str(qqid)
    return 1 + hash(s)%100


def jrrp(args, groupid, qqid):
    if not len(args) == 1: 
        return ""
    print(get_jrrp(qqid))
    return "[CQ:at,qq=%d]的人品值是：%d" %(qqid, get_jrrp(qqid))


