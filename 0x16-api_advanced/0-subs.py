#!/usr/bin/python3
"""
Module to query Reddit API and get the number of subscribers for a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers if the subreddit is valid, 0 otherwise.
    """
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Make the API request to get subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers)

    # Invalid subreddit returns a 404 status code
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
