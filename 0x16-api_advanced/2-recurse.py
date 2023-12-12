#!/usr/bin/python3
"""
Recursive function to query Reddit API and for a subreddit.
"""

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    Recursively query Reddit API to get titles of all
    hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store titles (default is None).
        after (str): Token for pagination (default is None).

    Returns:
        list: List containing titles of hot articles,
        or None if no results are found.
    """
    global after
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Initialize hot_list if not provided
    if hot_list is None:
        hot_list = []

    # Make the API request to get hot posts in the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if the subreddit is not valid
    if response.status_code == 404:
        print(f"The subreddit '{subreddit}' does not exist.")
        return None

    # Parse the JSON response to get post data
    data = response.json()

    # Extract titles and append to hot_list
    posts = data.get('data', {}).get('children', [])
    for post in posts:
        hot_list.append(post.get('data', {}).get('title'))

    # Recursive call for the next page
    after_token = data.get('data', {}).get('after')
    if after_token:
        recurse(subreddit, hot_list, after_token)

    return hot_list if hot_list else None
