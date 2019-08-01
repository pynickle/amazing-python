import requests
import re
import time
import random
import pprint


def youdict():
    res = []
    index = 0
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3858.0 Safari/537.36"}
    for i in range(1):
        index += 1
        r = requests.get(f"https://www.youdict.com/ciku/id_0_0_0_0_{i}.html", headers = headers)
        html = str(r.content, encoding="utf-8").replace("\n", "").replace("    ", "").replace('<span class="yd-kw-suffix">[英语单词大全]</span>', "")
        words = re.findall('<div class="caption"><h3 style="margin-top: 10px;"><a style="color:#333;" target="_blank" href="/w/.*?">(.*?)</a>[ ]?</h3><p>(.*?)</p></div>', html)
        # pprint.pprint(word)
        for word in words:
            res.append(word)
        if index%5 == 0:
            time.sleep(3 + random.random())
        else:
            time.sleep(1 + random.random())
    return res

if __name__ == "__main__": 
    print(youdict())
