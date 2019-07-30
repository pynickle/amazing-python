import requests
import json
import os
from lxml import etree
import numpy as np
import jieba
import wordcloud
from PIL import Image


stopwords = ["!", "！", "?", "？", "。", ".", ",", "，", "\\", "/"]
alice_mask = np.array(Image.open("../utils/wordcloud.jpg"))


def get_word():
    aid = input("enter the av: ")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    }
    url = "https://api.bilibili.com/x/web-interface/view?aid=" + aid
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        cid = json.loads(response.content.decode())["data"]["cid"]
        cid_url = "https://comment.bilibili.com/{}.xml".format(cid)

        result = requests.get(cid_url, headers=headers)
        comment_element = etree.HTML(result.content)
        d_list = comment_element.xpath("//d")

        if os.path.exists("./comment.txt"):
            os.remove("./comment.txt")
        with open("./comment.txt", "w", encoding="utf-8") as file:
            for d in d_list:
                file.write(d.xpath("./text()")[0] + "\n")


def chinese_jieba(txt):
    wordlist_jieba = jieba.cut(txt)
    txt_jieba = " ".join(wordlist_jieba)
    return txt_jieba


def make_cloud():
    with open('comment.txt', encoding="utf-8") as f:
        txt = f.read()
        txt = chinese_jieba(txt)
        wc = wordcloud.WordCloud(
            font_path='../utils/wc.ttf',
            max_words=30,
            stopwords=stopwords,
            mask=alice_mask,
            background_color="white",
        ).generate(txt)
        image = wc.to_file("bilibili.jpg")
        os.system("bilibili.jpg")


def main():
    get_word()
    make_cloud()


if __name__ == '__main__':
    main()
