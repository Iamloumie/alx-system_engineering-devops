#!/usr/bin/python3
"""
Script that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    a function that queries the Reddit API and prints the titles of the
        first 10 hot posts listed for a given subreddit.
    If not a valid subreddit, print None.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Define headers for the HTTP request, including User-Agent
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    # Define parameters for request, limiting the no of posts to 10
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return

    # Parse the JSON response and extract the 'data' section
    results = response.json().get("data")

    # Print the titles of top 10 posts
    [print(c.get("data").get("title")) for c in results.get("children")]
