#!/usr/bin/python3
"""
Script that queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and returns the number of subscribers
        (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.

    Hint: No authentication is necessary for most features of the Reddit API.
        If errors related to Too Many Requests is gotten,
            ensure a custom User-Agent is set.


    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
