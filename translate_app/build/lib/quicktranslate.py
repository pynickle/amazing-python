# -*- coding:UTF-8 -*-

from __future__ import print_function,unicode_literals
import requests
import json
from bs4 import BeautifulSoup
import execjs
import sys
import argparse


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}


def get_translate_youdao(word):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    Form_data = {
        "i": word,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1512399450582",
        "sign": "78181ebbdcb38de9b4a3f4cd1d38816b",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION",
        "typoResult": "false",
    }
    try:
        response = requests.post(url, data=Form_data)
        content = json.loads(response.text)
        result = content["translateResult"][0][0]["tgt"]
        return result
    except:
        return "wrong!"


def get_translate_baidu(word):
    url = "https://fanyi.baidu.com/sug"
    Form_data = {"kw": word}
    try:
        response = requests.post(url, data=Form_data, headers=headers)
        content = json.loads(response.text)
        result = content["data"][0]["v"]
        return result
    except:
        try:
            soup = BeautifulSoup(r.text, "lxml")
            correct = soup.find_all("a", class_="correct-link correct-query")
            Form_data = {"kw": correct[0]}
            response = requests.post(url, data=Form_data, headers=headers)
            content = json.loads(response.text)
            result = content["data"][0]["v"]
        except:
            return "wrong!"


class Py4Js:
    def __init__(self):
        self.ctx = execjs.compile(
            """ 
            function TL(a) { 
                var k = ""; 
                var b = 406644; 
                var b1 = 3293161072;       
                var jd = "."; 
                var $b = "+-a^+6"; 
                var Zb = "+-3^+b+-f";    
                for (var e = [], f = 0, g = 0; g < a.length; g++) { 
                    var m = a.charCodeAt(g); 
                    128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), 
                    e[f++] = m >> 18 | 240, 
                    e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, 
                    e[f++] = m >> 6 & 63 | 128), 
                    e[f++] = m & 63 | 128) 
                } 
                a = b; 
                for (f = 0; f < e.length; f++) a += e[f], 
                a = RL(a, $b); 
                a = RL(a, Zb); 
                a ^= b1 || 0; 
                0 > a && (a = (a & 2147483647) + 2147483648); 
                a %= 1E6; 
                return a.toString() + jd + (a ^ b) 
            };      
            function RL(a, b) { 
                var t = "a"; 
                var Yb = "+"; 
                for (var c = 0; c < b.length - 2; c += 3) { 
                    var d = b.charAt(c + 2), 
                    d = d >= t ? d.charCodeAt(0) - 87 : Number(d), 
                    d = b.charAt(c + 1) == Yb ? a >>> d: a << d; 
                    a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d 
                } 
                return a 
            } 
        """
        )

    def getTk(self, text):
        return self.ctx.call("TL", text)


def buildUrl(text, tk):
    baseUrl = "https://translate.google.cn/translate_a/single"
    baseUrl += "?client=t&"
    baseUrl += "s1=auto&"
    baseUrl += "t1=zh-CN&"
    baseUrl += "h1=zh-CN&"
    baseUrl += "dt=at&"
    baseUrl += "dt=bd&"
    baseUrl += "dt=ex&"
    baseUrl += "dt=ld&"
    baseUrl += "dt=md&"
    baseUrl += "dt=qca&"
    baseUrl += "dt=rw&"
    baseUrl += "dt=rm&"
    baseUrl += "dt=ss&"
    baseUrl += "dt=t&"
    baseUrl += "ie=UTF-8&"
    baseUrl += "oe=UTF-8&"
    baseUrl += "otf=1&"
    baseUrl += "pc=1&"
    baseUrl += "ssel=0&"
    baseUrl += "tsel=0&"
    baseUrl += "kc=2&"
    baseUrl += "tk=" + str(tk) + "&"
    baseUrl += "q=" + text
    return baseUrl


def get_translate_google(text):
    js = Py4Js()
    header = {
        "authority": "translate.google.cn",
        "method": "GET",
        "path": "",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cookie": "",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
        "x-client-data": "CIa2yQEIpbbJAQjBtskBCPqcygEIqZ3KAQioo8oBGJGjygE=",
    }
    url = buildUrl(text, js.getTk(text))
    res = ""
    try:
        r = requests.get(url)
        result = json.loads(r.text)
        if result[7] != None:
            try:
                correctText = (
                    result[7][0].replace("<b><i>", " ").replace("</i></b>", "")
                )
                correctUrl = buildUrl(correctText, js.getTk(correctText))
                correctR = requests.get(correctUrl)
                newResult = json.loads(correctR.text)
                res = newResult[0][0][0]
            except Exception as e:
                res = result[0][0][0]
        else:
            res = result[0][0][0]
    except:
        return "wrong!"
    finally:
        return res


def translate_main():
    parser = argparse.ArgumentParser(
        description="Translate with youdao,baidu and google")
    parser.add_argument('-t', '--trans', required=True,
                        help="Enter what you want to translate")
    args = parser.parse_args()
    translate_text = args.trans
    js = Py4Js()

    youdao = get_translate_youdao(translate_text)
    baidu = get_translate_baidu(translate_text)
    google = get_translate_google(translate_text)

    print("=========================")
    print("youdao translate result：", youdao)
    print("baidu translate result：", baidu)
    print("google translate result：", google)
    print("=========================")


if __name__ == "__main__":
    translate_main()
