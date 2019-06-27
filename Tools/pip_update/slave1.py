import pip
from subprocess import Popen
from pip._internal.utils.misc import get_installed_distributions
from redis import Redis


packages_list=get_installed_distributions()

def push_redis_list():
    r = Redis(host="127.0.0.1", port=6379)
    for package in packages_list:
        r.lpush("pip_packages", package.project_name)
        print("add package " + package.project_name)
    return

def pip_all():   
    r = Redis(host="127.0.0.1", port=6379)
    while True:
        package_name = r.lpop("pip_packages")
        package_name = package_name.decode("ascii")
        try:
            pip_upgrade = Popen("pip install --upgrade " + package_name + " -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com", shell=True)
            pip_upgrade.wait()
            print(f"update now : {package_name}")
        except:
            pass

def pip_main():
    machine = "slave"
    if machine=="master":
        push_redis_list()
    else:
        pip_all()

if __name__ == "__main__":
    pip_main()
