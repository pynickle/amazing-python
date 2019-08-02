import re
import time
import random
import os

import requests
import wordcloud
import numpy as np
from PIL import Image


alice_mask = np.array(Image.open("../utils/wordcloud.jpg"))

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}


def main(user="torvalds", repo="linux"):
    index = 1
    is_first = True
    latest_commit_id = ""
    commit_id_count = {}
    all_commit_id = ""
    while True:
        if is_first:
            url = "https://github.com/" + user + "/" + repo + "/commits/master"
            is_first = False
        else:
            url = "https://github.com/" + user + "/" + repo + \
                "/commits/master?after=" + latest_commit_id + \
                "+" + str(index * 35 - 1)
            index += 1
        print(url)
        r = requests.get(url, timeout=10, headers=headers)
        commit = re.findall(
            r'class="message js-navigation-open" data-pjax="true" href="/'
            + user
            + '/'
            + repo
            + '/commit/(.*)">.*</a>',
            r.text)
        # print(commit)
        if commit:
            latest_commit_id = commit[0]
            all_commit_id += "".join(commit)
        else:
            break
        time.sleep(random.randrange(1, 3))
    # print(all_commit_id)
    temp = []
    for i in all_commit_id:
        if i not in temp:
            commit_id_count[i] = all_commit_id.count(i)
            temp.append(i)
        else:
            continue
    print(all_commit_id)
    wc = wordcloud.WordCloud(
        font_path='../utils/wc.ttf',
        max_words=10,
        mask=alice_mask,
        background_color="white",
    ).generate_from_frequencies(commit_id_count)
    image = wc.to_file("./github_commit.jpg")
    # os.system("github_commit.jpg")


if __name__ == "__main__":
    user = input("enter the github username: ")
    repo = input("enter the github repo name: ")
    main(user=user, repo=repo)
