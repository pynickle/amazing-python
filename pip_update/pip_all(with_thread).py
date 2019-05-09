import pip
from subprocess import call,Popen
from pip._internal.utils.misc import get_installed_distributions
import threading
import queue as Queue


packages_list=get_installed_distributions()

class myThread(threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q

    # run
    def run(self):
        print("Starting " + self.name)
        while True:
            try:
                pip_all(self.name, self.q)
            except:
                break
        print("Exiting" + self.name)

def pip_all(threadName,q):   
    package_name=q.get()
    try:
        call("pip install --upgrade " + package_name.project_name, shell=True)
        print(f"update now : {package_name}")
    except:
        return

def pip_main():
    # our threads and queue
    threadList=[]
    for i in range(1,3):
        threadList.append("Thread-"+str(i))
    workQueue = Queue.Queue(1000)
    threads = []

    # start the threads
    for tName in threadList:
        thread = myThread(tName, workQueue)
        thread.start()
        threads.append(thread)

    # put the url
    for package in packages_list:
        workQueue.put(package)

    # wait for end
    for t in threads:
        t.join()

if __name__ == "__main__":
    pip_main()
