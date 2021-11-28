from selenium import webdriver
from urllib.request import urlopen
from urllib import error
from urllib.parse import urlparse
import requests


def get_links(url):
    """Find all links on page at the given url.

    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    browser = webdriver.Chrome('/Users/boom/Desktop/link-scanner/chromedriver')  # Change to your own path in bracket.
    browser.get(url)


def is_valid_url(url: str):
    try:
        opener = urlopen(url)
        opener.close()

    except (error.URLError, ValueError):
        return False
    except error.HTTPError as e:
        if e.code != 403:  # 403 forbidden = have but can't access
            return False
    return True


# def invalid_urls(urllist: List):
#     pass


if __name__ == "__main__":
    print(is_valid_url("https://www.thaizeed.net/"))
    print(is_valid_url("https://www.maimeeyoujing.co.th/"))
