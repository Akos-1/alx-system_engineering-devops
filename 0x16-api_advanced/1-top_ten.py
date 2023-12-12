#!/usr/bin/python3
"""
Module to query Reddit API and print the titles for a subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Make the API request to get hot posts in the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'        
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is not valid
    if response.status_code == 404:
        print("None")
        return

    # Parse the JSON response to get post data
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
