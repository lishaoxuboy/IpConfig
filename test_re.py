import subprocess
import re

# 执行windows命令
def exec_command(commands):
    if not commands:
        return
    # 子进程的标准输出设置为管道对象
    if isinstance(commands, str):
        commands = [commands]
    return_list = []
    for i in commands:
        p = subprocess.Popen(i, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        p.wait()
        # print(p.stdout.read())
        # print(p.stdout.readline())
        stdout = p.stdout.readlines()
        return_list.append(stdout)
    return return_list


def ping_ip(ip):
    res_list = exec_command(f'ping {ip}')[0]
    delay = int()
    for item in res_list:
        match_obj = re.match(r'.*(\S\S)ms', item, re.M | re.I)
        # ping通了
        if match_obj:
            try:
                delay += int(match_obj.group(1).replace('<', '').replace('=', ''))
            except ValueError:
                delay += 1
            continue

        # 100%丢失，不通
        if '数据包 : 已发送 = 4' in item:
            if '(100% 丢失)' in item:
                return delay
        if 'Ping 请求找不到主机' in item:
            return delay
    return 1 if int(delay / 4) < 1 else int(delay / 4)

print(ping_ip('www.baidu.com'))
print(ping_ip('www.dfslafjdslflsd.com'))
print(ping_ip('212.1313.1313.13212'))