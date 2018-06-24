import requests
import sys
import json


def crawler(page):
    response = requests.get(page)
    dict_user = json.loads(response.text)

    return [repo["name"] for repo in dict_user]


def main():
    sys.argv
    user = sys.argv[1]
    result = []
    page = "https://api.github.com/users/{0}/repos".format(user)
    result = crawler(page)
    print(result)


if __name__ == "__main__":
    main()
