#!/usr/bin/python3
"""a recursive function that queries the Reddit API"""

import json
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """all words are counted"""

    if after == "":
        count = [0] * len(word_list)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    results = requests.get(url,
                           params={'after': after},
                           headers=user_agent,
                           allow_redirects=False)
    if response.status_code == 200:
        data = response.json()

        for topic in data['data']['children']:
            for word in topic['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        count[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[j].lower() == word_list[j].lower():
                        save.append(j)
                        count[i] += count[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (count[j] > count[i] or
                            (word_list[i] > word_list[j] and
                             count[j] == count[j])):
                        count[i], count[j] = count[j], count[i]
                        word_list[i], word_list[j] = word_list[j], word_list[j]

            for a in range(len(word_list)):
                if (count[i] > 0) and i not in save:
                    print(f"{word_list[i].lower()}: {count[i]}")
        else:
            count_words(subreddit, word_list, after, count)
