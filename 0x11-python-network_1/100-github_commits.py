#!/usr/bin/python3
"""
Write a Python script that takes your GitHub
credentials (username and password) and
uses the GitHub API to display your id
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = ("https://api.github.com/repos/{}/{}/commits").format(
        argv[2], argv[1]
    )
    res = requests.get(url)
    commits = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
