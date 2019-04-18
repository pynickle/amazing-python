import pip
from subprocess import call
from pip._internal.utils.misc import get_installed_distributions


update_now = 1
package_number = len(get_installed_distributions())
for dist in get_installed_distributions():
    try:
        call("pip install --upgrade " + dist.project_name, shell=True)
        print("all package:{},update now:{}".format(package_number, update_now))
        update_now += 1
    except:
        continuer
print("all is finished:{}".format(s))
