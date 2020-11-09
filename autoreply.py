import time


def my_seek(key, msg):
    keys = key.split(" ")
    if len(keys) == 0 :
        return False
    for k in keys:
        if msg.find(k) == -1:
            return False
    return True


def get_autoans(msg):
	for i in autoans_pool:
		k,v,t = i
		if my_seek(k, msg) :
			if(time.time() - 600 >= t):
				print( t)
				i[2] = time.time()
				return v
	return ""

#autoans_pool = [["招生办 电话", "北师大招生办电话： 010-58807962", 0]]
#autoans_pool = []

def read_from_file():
    global autoans_pool
    autoans_pool = []
    f = open("autoreply.txt","r")
    lines = f.readlines()
    #print(lines)
    f.close()
    for line in lines:
        l = line[:-1].split('\t')
        if not len(l) == 2:
            continue
        autoans_pool.append(l + [0])
    #print(autoans_pool)
    


def write_to_file():
    lines = [i[0] + '\t' + i[1] for i in autoans_pool]
    print(lines)
    buf = '\n'.join(lines) + '\n'
    f = open("autoreply.txt","w")
    f.write(buf)
    f.close()


def add_auto_reply(args, groupid, qqid):
    if not qqid == 2234748103:
        return "权限不足"
    if not len(args) == 3:
        return "参数错误"
    autoans_pool.append([args[1], args[2], 0])
    write_to_file()
    return "添加成功"
    
    
read_from_file()
print(autoans_pool)