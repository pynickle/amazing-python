import pip
from subprocess import call
from pip._internal.utils.misc import get_installed_distributions


def pip_main():
    update_now = 1
    package_number = len(get_installed_distributions())
    for dist in get_installed_distributions():
        try:
            call(
                "pip install --upgrade "
                + dist.project_name
                + " -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com",
                shell=True,
            )
            print("all package:{},update now:{}".format(
                package_number, update_now))
            update_now += 1
        except Exception:
            continue
    print("all is finished:{}".format(s))


if __name__ == "__main__":
    pip_main()
