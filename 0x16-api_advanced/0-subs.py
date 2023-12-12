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

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response to get the number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 404:
        # Invalid subreddit returns a 404 status code
        print(f"The subreddit '{subreddit}' does not exist.")
        return 0
    else:
        # Handle other errors
        print(f"Error: {response.status_code}")
        return 0
