#!/usr/bin/python3
"""
Recursively query Reddit API to get titles
of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively query Reddit API to get titles of
    all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store titles (default is None).
        after (str): Token for pagination (default is None).

    Returns:
        list: List containing titles of hot articles,
        or None if no results are found.
    """
    # Initialize hot_list if not provided
    if hot_list is None:
        hot_list = []

    # Set User-Agent for API request
    user_agent = {'User-Agent': 'MyRedditBot/1.0'}

    # Make the API request to get hot posts in the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {}
    results = requests.get(
        url,
        params=params,
        headers=user_agent,
        allow_redirects=False
    )
    # Check if the request was successful (status code 200)
    if results.status_code == 200:
        # Extract data from the JSON response
        data = results.json().get("data")
        after_data = data.get("after")
        # Recursively call for the next page
        if after_data:
            recurse(subreddit, hot_list, after=after_data)

        # Extract titles and append to hot_list
        all_titles = data.get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list

    # Return None if the subreddit is not valid
    return None
