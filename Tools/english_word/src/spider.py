import requests
import re
import time
import random
import pprint
import os


headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3858.0 Safari/537.36"}

def youdict(threadName, q):
    res = []
    index = 0
    url = q.get(timeout = 2)
    index += 1
    r = requests.get(url, headers = headers, timeout = 5)
    html = str(r.content, encoding="utf-8").replace("\n", "").replace("    ", "").replace('<span class="yd-kw-suffix">[英语单词大全]</span>', "")
    words = re.findall('<div class="caption"><h3 style="margin-top: 10px;"><a style="color:#333;" target="_blank" href="/w/.*?">(.*?)</a>[ ]?</h3><p>(.*?)</p></div>', html)

    for word in words:
        res.append(word)
    if index%5 == 0:
        time.sleep(3 + random.random())
    else:
        time.sleep(1 + random.random())
    return res

def hujiang(threadName, q):
    res = []
    index = 0
    url = q.get(timeout = 2)
    
    index += 1
    r = requests.get(url, headers=headers, timeout=5)
    html = str(r.content, encoding="utf-8").replace("\n", "").replace("    ", "").replace('<span class="yd-kw-suffix">[英语单词大全]</span>', "")
    words = re.findall('<li class="clearfix"><a href="/ciku/(.*?)/" target="_blank">.*?</a><span>(.*?)</span></li>', html)
    for word in words:
        res.append(word)
        
    if index%5 == 0:
        time.sleep(3 + random.random())
    else:
        time.sleep(1 + random.random())
    return res

if __name__ == "__main__":
    main()
