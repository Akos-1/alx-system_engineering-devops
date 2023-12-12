#!/usr/bin/python3
"""a recursive function that queries the Reddit API"""

import requests


def count_words(subreddit, word_list, after="", count=None):
    """all words are counted"""

    if after == "":
        count = [0] * len(word_list)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    params = {'after': after}
    results = requests.get(
        url,
        params=params,
        headers=user_agent,
        allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json()

        for topic in data['data']['children']:
            for word in topic['data']['title'].split():
                for a in range(len(word_list)):
                    if word_list[a].lower() == word.lower():
                        count[a] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for a in range(len(word_list)):
                for b in range(a + 1, len(word_list)):
                    if word_list[a].lower() == word_list[b].lower():
                        save.append(b)
                        count[a] += count[b]

            for a in range(len(word_list)):
                for b in range(a, len(word_list)):
                    if (count[b] > count[a] or
                            (word_list[a] > word_list[b] and
                             count[b] == count[a])):
                        count[a], count[b] = count[b], count[a]
                        word_list[a], word_list[b] = word_list[b], word_list[a]

            for a in range(len(word_list)):
                if (count[a] > 0) and a not in save:
                    print(f"{word_list[a].lower()}: {count[a]}")
        else:
            count_words(subreddit, word_list, after, count)
