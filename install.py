import os
import sys
HEADER = '\033[95m'
OKBLUE = '\033[94m'     
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'    
BOLD = '\033[1m'         
UNDERLINE = '\033[4m'
print(OKBLUE+"======================================================")
print(WARNING+"申请储存权限指令")
print(OKBLUE+'termux-setup-storage')
print(OKBLUE+"======================================================")
run = input(OKBLUE+"是否需要安装服务 [Y/N] ")

if run == "n":
    sys.exit()

os.system("cd ~")
#更新包
os.system("apt update && apt upgrade -y")
#开始安装程序
print(OKGREEN+"开始安装服务程序")
os.system("apt install vim nginx php php-fpm")
os.system("mv $PREFIX/etc/nginx/nginx.conf $PREFIX/etc/nginx/nginx.conf.bak")
#复制配置文件
os.system("cp ./conf/nginx.conf $PREFIX/etc/nginx/nginx.conf")
os.system("mv $PREFIX/etc/php-fpm.d/www.conf $PREFIX/etc/php-fpm.d/www.conf.bak")
os.system("cp ./conf/www.conf $PREFIX/etc/php-fpm.d/www.conf")
#写入网站目录
www_dir = "/sdcard/www"
if os.path.exists(www_dir):
    print(OKBLUE+"======================================================")
    print(WARNING+"%s已存在，请移出该目录下的文件并删除www"%www_dir)
    print(OKBLUE+"======================================================")

    os.system("mkdir /sdcard/www")
    if os.path.exists(www_dir):
        print(OKBLUE+"======================================================")
        print(WARNING+"目录www创建成功，目录地址%s\n"%www_dir)
        print(OKBLUE+"======================================================")
    else:
        print(OKBLUE+"======================================================")
        print(WARNING+"目录www创建失败，可能是没有获取到储存权限，请执行termux-setup-storage后重试")
        print(OKBLUE+"======================================================")

#启动服务
os.system("nginx")
os.system("php-fpm")
print(OKBLUE+"======================================================")
print(OKGREEN+"网站地址为："+UNDERLINE+"http://127.0.0.1:8080\033[0m")
print(OKGREEN+"将项目放入站点目录www，浏览器输入地址即可访问，如没有www可手动创建")
print(OKBLUE+"======================================================")
