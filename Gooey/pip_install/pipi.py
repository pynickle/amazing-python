import argparse
import sys
from subprocess import call
from pip._internal.utils.misc import get_installed_distributions

ALIYUN = "http://mirrors.aliyun.com/pypi/simple"
ALIYUNHOST = "mirrors.aliyun.com"

ZHONGGUOKEJIDAXUE = "https://pypi.mirrors.ustc.edu.cn/simple"
ZHONGGUOKEJIDAXUEHOST = "pypi.mirrors.ustc.edu.cn"

DOUBAN = "http://pypi.douban.com/simple"
DOUBANHOST = "pypi.douban.com"

QINGHUADAXUE = "https://pypi.tuna.tsinghua.edu.cn/simple"
QINGHUADAXUEHOST = "pypi.tuna.tsinghua.edu.cn"

ZHONGGUOKEXUEJISHUDAXUE = "http://pypi.mirrors.ustc.edu.cn/simple"
ZHONGGUOKEXUEJISHUDAXUEHOST = "pypi.mirrors.ustc.edu.cn"


def pip_main():
    update_now = 1
    package_number = len(get_installed_distributions())

    parser = argparse.ArgumentParser(
        description="使用镜像下载python第三方库")
    parser.add_argument("-p", "--package", help="你想要下载的库")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--aliyun", help="使用阿里云镜像", action="store_true")
    group.add_argument("-k", "--keji", help="使用中国科技大学镜像", action="store_true")
    group.add_argument("-d", "--douban", help="使用豆瓣镜像", action="store_true")
    group.add_argument("-q", "--qinghua", help="使用清华大学镜像", action="store_true")
    group.add_argument("-j", "--jishu", help="使用中国科学技术大学镜像",
                       action="store_true")

    args = parser.parse_args()
    package = args.package
    if args.aliyun:
        website = ALIYUN
        host = ALIYUNHOST
    elif args.keji:
        website = ZHONGGUOKEJIDAXUE
        host = ZHONGGUOKEJIDAXUEHOST
    elif args.douban:
        website = DOUBAN
        host = DOUBANHOST
    elif args.qinghua:
        website = QINGHUADAXUE
        host = QINGHUADAXUEHOST
    elif args.jishu:
        website = ZHONGGUOKEXUEJISHUDAXUE
        host = ZHONGGUOKEXUEJISHUDAXUEHOST
    else:
        print("unknown mirror")
        sys.exit()

    print("website : " + website)
    print("host : " + host)
    print("package : " + package)

    cmd = "pip install --upgrade " + package + \
        " -i " + website + " --trusted-host " + host
    try:
        call(cmd, shell=True)
        print("update...")
    except Exception as e:
        print("error occured!", e)


if __name__ == "__main__":
    pip_main()
